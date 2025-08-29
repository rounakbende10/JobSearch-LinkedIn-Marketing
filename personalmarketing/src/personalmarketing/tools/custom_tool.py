from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import json
import os

class LinkedInPostAnalyzerInput(BaseModel):
    post_content: str = Field(..., description="The LinkedIn post content to analyze")
    target_audience: str = Field(..., description="The target audience for the post")

class LinkedInPostAnalyzerOutput(BaseModel):
    engagement_score: int = Field(..., description="Predicted engagement score (1-10)")
    hashtag_suggestions: list = Field(..., description="Suggested hashtags for the post")
    optimization_tips: list = Field(..., description="Tips to improve the post")
    target_audience_match: str = Field(..., description="How well the post matches the target audience")

class LinkedInPostAnalyzer(BaseTool):
    name: str = "LinkedIn Post Analyzer"
    description: str = "Analyzes LinkedIn posts for engagement potential and provides optimization suggestions for senior AI/ML engineering roles"
    
    def _run(self, post_content: str, target_audience: str) -> str:
        """
        Analyze a LinkedIn post for engagement potential and provide optimization suggestions for senior AI/ML engineering roles.
        """
        # This is a simplified analysis - in a real implementation, you might use
        # LinkedIn's API or machine learning models for more accurate predictions
        
        # Basic engagement scoring based on content characteristics
        score = 5  # Base score
        
        # Check for engagement triggers
        if "?" in post_content:
            score += 1
        if "!" in post_content:
            score += 1
        if len(post_content.split()) > 50:
            score += 1
        if "#" in post_content:
            score += 1
        if "https://" in post_content or "http://" in post_content:
            score += 1
            
        # Suggested hashtags based on content for senior AI/ML engineering
        hashtags = []
        content_lower = post_content.lower()
        
        # Senior AI/ML Engineering specific hashtags
        if "llm" in content_lower or "large language model" in content_lower:
            hashtags.extend(["#LLM", "#LargeLanguageModels", "#AI", "#MachineLearning"])
        if "rag" in content_lower or "retrieval augmented generation" in content_lower:
            hashtags.extend(["#RAG", "#RetrievalAugmentedGeneration", "#AI", "#NLP"])
        if "mlops" in content_lower or "machine learning operations" in content_lower:
            hashtags.extend(["#MLOps", "#MachineLearning", "#DevOps", "#AIEngineering"])
        if "production" in content_lower or "deployment" in content_lower:
            hashtags.extend(["#ProductionML", "#MLDeployment", "#AIEngineering", "#MLOps"])
        if "architecture" in content_lower or "system design" in content_lower:
            hashtags.extend(["#SystemArchitecture", "#AIArchitecture", "#Engineering", "#TechLeadership"])
        if "senior" in content_lower or "lead" in content_lower:
            hashtags.extend(["#SeniorEngineer", "#TechLeadership", "#EngineeringLeadership", "#AIEngineering"])
        if "pytorch" in content_lower or "tensorflow" in content_lower:
            hashtags.extend(["#PyTorch", "#TensorFlow", "#DeepLearning", "#AI"])
        if "aws" in content_lower or "gcp" in content_lower or "azure" in content_lower:
            hashtags.extend(["#AWS", "#GCP", "#Azure", "#CloudComputing", "#MLOps"])
        if "langchain" in content_lower or "langgraph" in content_lower:
            hashtags.extend(["#LangChain", "#LangGraph", "#AI", "#LLM"])
        if "healthcare" in content_lower or "clinical" in content_lower:
            hashtags.extend(["#HealthcareAI", "#ClinicalAI", "#HealthTech", "#AI"])
        if "finance" in content_lower or "fintech" in content_lower:
            hashtags.extend(["#FinTech", "#FinanceAI", "#AI", "#MachineLearning"])
            
        # Add general senior engineering hashtags
        hashtags.extend(["#LinkedIn", "#AIEngineering", "#MachineLearning", "#SeniorEngineer", "#TechLeadership"])
        
        # Optimization tips for senior engineering content
        tips = []
        if score < 7:
            tips.append("Add technical depth to demonstrate senior-level expertise")
            tips.append("Include relevant technical hashtags")
            tips.append("Add a call-to-action for technical discussion")
        if len(post_content) < 100:
            tips.append("Expand on technical concepts for better engagement")
        if "?" not in post_content:
            tips.append("Ask a technical question to encourage comments")
        if "architecture" not in content_lower and "system" not in content_lower:
            tips.append("Consider adding system architecture insights")
        if "production" not in content_lower and "deployment" not in content_lower:
            tips.append("Include production deployment considerations")
            
        result = {
            "engagement_score": min(score, 10),
            "hashtag_suggestions": hashtags[:5],
            "optimization_tips": tips,
            "target_audience_match": "Good" if score >= 7 else "Needs improvement"
        }
        
        return json.dumps(result, indent=2)

class InnovationTrackerInput(BaseModel):
    topic: str = Field(..., description="The AI/ML topic to track for latest innovations")
    timeframe: str = Field(..., description="Timeframe for innovation tracking (e.g., 'last 3 months', 'last 6 months')")

class InnovationTrackerOutput(BaseModel):
    latest_innovations: list = Field(..., description="Latest innovations and developments")
    trending_topics: list = Field(..., description="Currently trending topics")
    emerging_technologies: list = Field(..., description="Emerging technologies to watch")
    industry_insights: list = Field(..., description="Key industry insights and trends")

class InnovationTracker(BaseTool):
    name: str = "AI/ML Innovation Tracker"
    description: str = "Tracks latest innovations, trends, and developments in AI/ML engineering for senior-level content creation"
    
    def _run(self, topic: str, timeframe: str) -> str:
        """
        Track latest innovations and trends in AI/ML engineering for content creation.
        """
        # This tool would integrate with real-time APIs in production
        # For now, providing structured guidance for innovation tracking
        
        topic_lower = topic.lower()
        
        # Latest innovations based on topic
        innovations = []
        trending_topics = []
        emerging_technologies = []
        industry_insights = []
        
        if "llm" in topic_lower or "large language model" in topic_lower:
            innovations = [
                "Multi-modal LLMs (GPT-4V, Claude 3 Vision)",
                "LLM reasoning improvements (Chain-of-Thought, Tree-of-Thoughts)",
                "Efficient fine-tuning techniques (QLoRA, DoRA)",
                "LLM safety and alignment research",
                "Open-source LLM developments (Llama 3, Mistral, Gemma)"
            ]
            trending_topics = [
                "LLM agents and autonomous systems",
                "RAG system optimizations",
                "LLM evaluation and benchmarking",
                "Cost optimization for LLM deployments"
            ]
            emerging_technologies = [
                "Retrieval-Augmented Generation (RAG) 2.0",
                "LLM orchestration frameworks",
                "Edge LLM deployment",
                "Federated learning for LLMs"
            ]
            
        elif "mlops" in topic_lower or "production ml" in topic_lower:
            innovations = [
                "MLOps automation and CI/CD for ML",
                "Model monitoring and observability",
                "Feature store implementations",
                "ML model versioning and governance",
                "ML pipeline orchestration tools"
            ]
            trending_topics = [
                "MLOps at scale",
                "Model drift detection and retraining",
                "ML security and privacy",
                "ML cost optimization"
            ]
            emerging_technologies = [
                "MLOps platforms (Weights & Biases, MLflow, Kubeflow)",
                "AutoML and automated feature engineering",
                "ML model compression and optimization",
                "ML model serving and inference optimization"
            ]
            
        elif "rag" in topic_lower or "retrieval augmented generation" in topic_lower:
            innovations = [
                "Advanced RAG architectures",
                "Multi-modal RAG systems",
                "RAG evaluation frameworks",
                "RAG optimization techniques",
                "RAG for enterprise applications"
            ]
            trending_topics = [
                "RAG system performance optimization",
                "RAG for real-time applications",
                "RAG security and privacy",
                "RAG integration with existing systems"
            ]
            emerging_technologies = [
                "Vector databases (Pinecone, Weaviate, Chroma)",
                "RAG orchestration frameworks",
                "Hybrid search and retrieval methods",
                "RAG for edge computing"
            ]
            
        elif "healthcare" in topic_lower or "clinical" in topic_lower:
            innovations = [
                "AI for medical imaging and diagnosis",
                "Clinical decision support systems",
                "Drug discovery and development",
                "Personalized medicine and genomics",
                "Healthcare data privacy and security"
            ]
            trending_topics = [
                "AI in telemedicine",
                "Clinical trial optimization",
                "Healthcare workflow automation",
                "AI for patient monitoring"
            ]
            emerging_technologies = [
                "Federated learning for healthcare",
                "AI-powered medical devices",
                "Healthcare-specific LLMs",
                "AI for drug repurposing"
            ]
            
        else:
            # General AI/ML innovations
            innovations = [
                "Foundation models and their applications",
                "AI safety and alignment research",
                "Multi-modal AI systems",
                "AI for scientific discovery",
                "Sustainable AI and green computing"
            ]
            trending_topics = [
                "AI regulation and governance",
                "AI ethics and responsible AI",
                "AI for climate change",
                "AI democratization and accessibility"
            ]
            emerging_technologies = [
                "Quantum machine learning",
                "Neuromorphic computing",
                "AI for edge devices",
                "Federated and distributed AI"
            ]
            
        industry_insights = [
            "Increased focus on AI safety and responsible development",
            "Growing demand for MLOps and production ML expertise",
            "Rise of AI-first companies and AI-native applications",
            "Convergence of AI with other emerging technologies",
            "Growing importance of AI governance and compliance"
        ]
        
        result = {
            "latest_innovations": innovations,
            "trending_topics": trending_topics,
            "emerging_technologies": emerging_technologies,
            "industry_insights": industry_insights,
            "tracking_timeframe": timeframe,
            "topic": topic
        }
        
        return json.dumps(result, indent=2)

class ResearchTopicAnalyzerInput(BaseModel):
    topic: str = Field(..., description="The research topic to analyze")
    field: str = Field(..., description="The field of research")

class ResearchTopicAnalyzerOutput(BaseModel):
    publication_potential: str = Field(..., description="Assessment of publication potential")
    target_journals: list = Field(..., description="Suggested target journals/platforms")
    research_gaps: list = Field(..., description="Identified research gaps")
    methodology_suggestions: list = Field(..., description="Suggested research methodologies")

class ResearchTopicAnalyzer(BaseTool):
    name: str = "Research Topic Analyzer"
    description: str = "Analyzes research topics for publication potential and provides suggestions for senior AI/ML engineering content"
    
    def _run(self, topic: str, field: str) -> str:
        """
        Analyze a research topic for publication potential and provide suggestions for senior AI/ML engineering content.
        """
        # This is a simplified analysis - in a real implementation, you might use
        # academic databases or research APIs for more accurate assessments
        
        # Basic publication potential assessment for senior AI/ML engineering
        potential = "Medium"
        if any(word in topic.lower() for word in ["llm", "large language model", "rag", "retrieval augmented generation", "mlops", "production ml"]):
            potential = "High"
        elif any(word in topic.lower() for word in ["architecture", "system design", "deployment", "engineering", "senior"]):
            potential = "High"
        elif any(word in topic.lower() for word in ["ai", "machine learning", "deep learning", "neural networks"]):
            potential = "Medium"
        else:
            potential = "Low"
            
        # Suggested target journals/platforms for senior AI/ML engineering
        journals = []
        if "llm" in field.lower() or "large language model" in field.lower():
            journals.extend(["arXiv", "Towards Data Science", "AI Engineering Blog", "Medium", "TechCrunch"])
        elif "mlops" in field.lower() or "production" in field.lower():
            journals.extend(["MLOps Community", "Towards Data Science", "Medium", "Engineering Blogs"])
        elif "architecture" in field.lower() or "system design" in field.lower():
            journals.extend(["System Design Blog", "Engineering Blogs", "Medium", "Tech Publications"])
        elif "healthcare" in field.lower() or "clinical" in field.lower():
            journals.extend(["Healthcare AI Blog", "Clinical AI Publications", "Medium", "HealthTech Blogs"])
        elif "finance" in field.lower() or "fintech" in field.lower():
            journals.extend(["FinTech Blogs", "Finance AI Publications", "Medium", "TechCrunch"])
        else:
            journals.extend(["Medium", "Towards Data Science", "Engineering Blogs", "Tech Publications"])
            
        # Research gaps and methodology suggestions for senior engineering
        gaps = [
            "Limited research on production deployment strategies",
            "Need for more system architecture case studies",
            "Gap in senior-level engineering best practices",
            "Limited research on MLOps at scale"
        ]
        
        methodologies = [
            "System architecture case study analysis",
            "Production deployment case studies",
            "Engineering best practices documentation",
            "Technical implementation guides"
        ]
        
        result = {
            "publication_potential": potential,
            "target_journals": journals,
            "research_gaps": gaps,
            "methodology_suggestions": methodologies
        }
        
        return json.dumps(result, indent=2)

class ResumeOptimizerInput(BaseModel):
    resume_content: str = Field(..., description="The resume content to optimize")
    target_role: str = Field(..., description="The target role/position")

class ResumeOptimizerOutput(BaseModel):
    optimization_suggestions: list = Field(..., description="Suggestions to optimize the resume")
    keyword_matches: list = Field(..., description="Keywords that match the target role")
    missing_keywords: list = Field(..., description="Keywords that should be added")
    overall_score: int = Field(..., description="Overall optimization score (1-10)")

class ResumeOptimizer(BaseTool):
    name: str = "Resume Optimizer"
    description: str = "Analyzes and optimizes resume content for senior AI/ML engineering roles"
    
    def _run(self, resume_content: str, target_role: str) -> str:
        """
        Analyze and optimize resume content for senior AI/ML engineering roles.
        """
        # This is a simplified analysis - in a real implementation, you might use
        # ATS systems or job description APIs for more accurate matching
        
        resume_lower = resume_content.lower()
        role_lower = target_role.lower()
        
        # Common keywords for senior AI/ML engineering roles
        role_keywords = {
            "senior ai engineer": ["llm", "large language model", "rag", "retrieval augmented generation", "mlops", "production deployment", "system architecture", "senior", "lead", "mentor", "architect", "design", "scale", "optimization"],
            "senior ml engineer": ["machine learning", "deep learning", "pytorch", "tensorflow", "mlops", "production", "deployment", "senior", "lead", "mentor", "architecture", "optimization", "performance"],
            "ai ml engineer": ["ai", "machine learning", "llm", "deep learning", "pytorch", "tensorflow", "mlops", "production", "deployment", "senior", "lead", "architecture"],
            "senior machine learning engineer": ["machine learning", "deep learning", "mlops", "production", "deployment", "senior", "lead", "mentor", "architecture", "optimization", "scale"],
            "ai engineer": ["ai", "machine learning", "llm", "deep learning", "pytorch", "tensorflow", "mlops", "production", "deployment", "architecture"]
        }
        
        # Find matching keywords
        matching_keywords = []
        missing_keywords = []
        
        for role, keywords in role_keywords.items():
            if role in role_lower:
                for keyword in keywords:
                    if keyword in resume_lower:
                        matching_keywords.append(keyword)
                    else:
                        missing_keywords.append(keyword)
                break
                
        # Optimization suggestions for senior roles
        suggestions = []
        if len(missing_keywords) > 0:
            suggestions.append(f"Add missing senior-level keywords: {', '.join(missing_keywords[:3])}")
        if len(resume_content.split()) < 300:
            suggestions.append("Expand on senior-level responsibilities and leadership experience")
        if "quantified" not in resume_lower and "metrics" not in resume_lower:
            suggestions.append("Add quantified achievements and performance metrics")
        if "senior" not in resume_lower and "lead" not in resume_lower:
            suggestions.append("Emphasize senior-level responsibilities and leadership")
        if "architecture" not in resume_lower and "design" not in resume_lower:
            suggestions.append("Highlight system architecture and design experience")
        if "mentor" not in resume_lower and "lead" not in resume_lower:
            suggestions.append("Include mentoring and team leadership experience")
            
        # Calculate overall score
        score = 5  # Base score
        score += len(matching_keywords) * 2
        score -= len(missing_keywords)
        score = max(1, min(10, score))
        
        result = {
            "optimization_suggestions": suggestions,
            "keyword_matches": matching_keywords,
            "missing_keywords": missing_keywords[:5],
            "overall_score": score
        }
        
        return json.dumps(result, indent=2)
