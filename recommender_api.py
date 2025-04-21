import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re

class SHLRecommender:
    def __init__(self, data_path='shl_assessments_complete.json'):
        with open(data_path) as f:
            self.data = json.load(f)
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self._prepare_data()

    def _parse_duration(self, duration_str):
        """Parse duration string and return maximum minutes"""
        if not duration_str or duration_str.lower() == 'not specified':
            return float('inf')  # Treat as no duration limit
        
        # Extract numbers from duration string
        numbers = re.findall(r'\d+', duration_str)
        if not numbers:
            return float('inf')
        
        # Return the highest number in case of ranges
        return max(map(int, numbers))

    def _prepare_data(self):
        """Prepare assessment data for recommendation"""
        self.assessments = self.data['assessments']
        
        # Create text for embedding
        self.texts = []
        for assessment in self.assessments:
            text = f"{assessment['name']} {assessment['description']} "
            text += f"Skills: {', '.join(assessment.get('skills_tested', []))} "
            text += f"Use cases: {', '.join(assessment.get('use_cases', []))}"
            self.texts.append(text)
        
        # Generate embeddings
        self.embeddings = self.model.encode(self.texts)

    def recommend(self, query, top_k=5, category=None, duration_max=None):
        """Get recommendations based on query and filters"""
        query_embedding = self.model.encode([query])
        similarities = cosine_similarity(query_embedding, self.embeddings)[0]
        
        results = []
        for idx, score in enumerate(similarities):
            assessment = self.assessments[idx]
            
            # Apply filters
            if category and assessment['category'] != category:
                continue
                
            if duration_max is not None:
                duration = self._parse_duration(assessment['duration'])
                if duration > duration_max:
                    continue
            
            results.append({
                **assessment,
                'score': float(score)
            })
        
        # Sort by similarity score
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:top_k]

    def get_categories(self):
        """Get list of available categories"""
        return self.data['metadata']['categories']