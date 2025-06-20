
import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { MessageCircle, BarChart3, BookOpen, Brain, Sparkles, Users, ChevronRight } from "lucide-react";
import ChatbotInterface from "@/components/ChatbotInterface";
import MLDashboard from "@/components/MLDashboard";

const Index = () => {
  const [activeInterface, setActiveInterface] = useState<'home' | 'chatbot' | 'ml'>('home');

  const renderHomeInterface = () => (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-cyan-50">
      {/* Header */}
      <header className="bg-white/80 backdrop-blur-sm border-b border-blue-100 sticky top-0 z-50">
        <div className="container mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-gradient-to-r from-blue-500 to-cyan-600 rounded-lg flex items-center justify-center">
                <Brain className="w-6 h-6 text-white" />
              </div>
              <div>
                <h1 className="text-xl font-bold text-gray-900">ASD Web Portal</h1>
                <p className="text-sm text-gray-600">AI-Powered Autism Support Platform</p>
              </div>
            </div>
            <Badge variant="secondary" className="bg-cyan-100 text-cyan-700">
              <Sparkles className="w-3 h-3 mr-1" />
              AI Enhanced
            </Badge>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="container mx-auto px-6 py-16">
        <div className="text-center max-w-4xl mx-auto">
          <h1 className="text-5xl font-bold text-gray-900 mb-6 leading-tight">
            Comprehensive <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-cyan-600">ASD Support</span> Platform
          </h1>
          <p className="text-xl text-gray-600 mb-8 leading-relaxed">
            Combining AI-powered assistance with advanced machine learning insights to support individuals, families, and researchers in the autism community.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Button 
              onClick={() => setActiveInterface('chatbot')} 
              size="lg" 
              className="bg-gradient-to-r from-blue-500 to-blue-600 hover:from-blue-600 hover:to-blue-700 text-white px-8 py-3"
            >
              <MessageCircle className="w-5 h-5 mr-2" />
              Start Chatting
              <ChevronRight className="w-4 h-4 ml-2" />
            </Button>
            <Button 
              onClick={() => setActiveInterface('ml')} 
              variant="outline" 
              size="lg" 
              className="border-cyan-200 text-cyan-700 hover:bg-cyan-50 px-8 py-3"
            >
              <BarChart3 className="w-5 h-5 mr-2" />
              View ML Insights
            </Button>
          </div>
        </div>
      </section>

      {/* Features Grid */}
      <section className="container mx-auto px-6 py-16">
        <div className="grid md:grid-cols-2 gap-8 max-w-6xl mx-auto">
          {/* Chatbot Card */}
          <Card className="group hover:shadow-xl transition-all duration-300 cursor-pointer border-blue-100 hover:border-blue-200" onClick={() => setActiveInterface('chatbot')}>
            <CardHeader className="pb-4">
              <div className="w-12 h-12 bg-gradient-to-r from-blue-500 to-blue-600 rounded-lg flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                <MessageCircle className="w-6 h-6 text-white" />
              </div>
              <CardTitle className="text-2xl text-gray-900">ASD Assistant Chatbot</CardTitle>
              <CardDescription className="text-gray-600">
                Interactive AI assistant powered by Gemini Flash 2.0 with comprehensive autism-related knowledge
              </CardDescription>
            </CardHeader>
            <CardContent>
              <ul className="space-y-2 text-gray-600">
                <li className="flex items-center">
                  <div className="w-2 h-2 bg-blue-400 rounded-full mr-3"></div>
                  Answer autism-related questions instantly
                </li>
                <li className="flex items-center">
                  <div className="w-2 h-2 bg-blue-400 rounded-full mr-3"></div>
                  FAISS vector database for accurate responses
                </li>
                <li className="flex items-center">
                  <div className="w-2 h-2 bg-blue-400 rounded-full mr-3"></div>
                  Reference-backed information
                </li>
                <li className="flex items-center">
                  <div className="w-2 h-2 bg-blue-400 rounded-full mr-3"></div>
                  Modern conversation interface
                </li>
              </ul>
              <Button className="w-full mt-6 bg-blue-500 hover:bg-blue-600" onClick={() => setActiveInterface('chatbot')}>
                Open Chatbot
                <ChevronRight className="w-4 h-4 ml-2" />
              </Button>
            </CardContent>
          </Card>

          {/* ML Dashboard Card */}
          <Card className="group hover:shadow-xl transition-all duration-300 cursor-pointer border-cyan-100 hover:border-cyan-200" onClick={() => setActiveInterface('ml')}>
            <CardHeader className="pb-4">
              <div className="w-12 h-12 bg-gradient-to-r from-cyan-500 to-cyan-600 rounded-lg flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                <BarChart3 className="w-6 h-6 text-white" />
              </div>
              <CardTitle className="text-2xl text-gray-900">ML Insights Dashboard</CardTitle>
              <CardDescription className="text-gray-600">
                Advanced machine learning visualizations and autism likelihood prediction insights
              </CardDescription>
            </CardHeader>
            <CardContent>
              <ul className="space-y-2 text-gray-600">
                <li className="flex items-center">
                  <div className="w-2 h-2 bg-cyan-400 rounded-full mr-3"></div>
                  Feature importance analysis
                </li>
                <li className="flex items-center">
                  <div className="w-2 h-2 bg-cyan-400 rounded-full mr-3"></div>
                  Classification results visualization
                </li>
                <li className="flex items-center">
                  <div className="w-2 h-2 bg-cyan-400 rounded-full mr-3"></div>
                  Interactive data exploration
                </li>
                <li className="flex items-center">
                  <div className="w-2 h-2 bg-cyan-400 rounded-full mr-3"></div>
                  Research documentation
                </li>
              </ul>
              <Button className="w-full mt-6 bg-cyan-500 hover:bg-cyan-600" onClick={() => setActiveInterface('ml')}>
                View Dashboard
                <ChevronRight className="w-4 h-4 ml-2" />
              </Button>
            </CardContent>
          </Card>
        </div>
      </section>

      {/* Statistics Section */}
      <section className="bg-white/50 backdrop-blur-sm border-y border-blue-100">
        <div className="container mx-auto px-6 py-16">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Platform Impact</h2>
            <p className="text-gray-600 max-w-2xl mx-auto">
              Supporting the autism community through advanced AI and machine learning technologies
            </p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-4xl mx-auto">
            <div className="text-center">
              <div className="w-16 h-16 bg-gradient-to-r from-blue-500 to-cyan-600 rounded-full flex items-center justify-center mx-auto mb-4">
                <Users className="w-8 h-8 text-white" />
              </div>
              <h3 className="text-3xl font-bold text-gray-900 mb-2">24/7</h3>
              <p className="text-gray-600">AI Assistant Availability</p>
            </div>
            <div className="text-center">
              <div className="w-16 h-16 bg-gradient-to-r from-cyan-500 to-blue-600 rounded-full flex items-center justify-center mx-auto mb-4">
                <BookOpen className="w-8 h-8 text-white" />
              </div>
              <h3 className="text-3xl font-bold text-gray-900 mb-2">1000+</h3>
              <p className="text-gray-600">Research Data Points</p>
            </div>
            <div className="text-center">
              <div className="w-16 h-16 bg-gradient-to-r from-blue-500 to-cyan-600 rounded-full flex items-center justify-center mx-auto mb-4">
                <Brain className="w-8 h-8 text-white" />
              </div>
              <h3 className="text-3xl font-bold text-gray-900 mb-2">95%</h3>
              <p className="text-gray-600">ML Model Accuracy</p>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white">
        <div className="container mx-auto px-6 py-12">
          <div className="text-center">
            <div className="flex items-center justify-center space-x-3 mb-4">
              <div className="w-8 h-8 bg-gradient-to-r from-blue-500 to-cyan-600 rounded-lg flex items-center justify-center">
                <Brain className="w-5 h-5 text-white" />
              </div>
              <h3 className="text-xl font-bold">ASD Web Portal</h3>
            </div>
            <p className="text-gray-400 mb-6 max-w-2xl mx-auto">
              Empowering the autism community through innovative AI technology and comprehensive machine learning insights.
            </p>
            <div className="border-t border-gray-800 pt-6">
              <p className="text-gray-500 text-sm">© 2024 ASD Web Portal. Built with care for the autism community.</p>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );

  if (activeInterface === 'chatbot') {
    return <ChatbotInterface onBack={() => setActiveInterface('home')} />;
  }

  if (activeInterface === 'ml') {
    return <MLDashboard onBack={() => setActiveInterface('home')} />;
  }

  return renderHomeInterface();
};

export default Index;
