
import { useState, useRef, useEffect } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card, CardContent } from "@/components/ui/card";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Badge } from "@/components/ui/badge";
import { ArrowLeft, Send, MessageCircle, Brain, Sparkles, User, Bot, Clock } from "lucide-react";

interface Message {
  id: string;
  text: string;
  isUser: boolean;
  timestamp: Date;
  references?: string[];
}

interface ChatbotInterfaceProps {
  onBack: () => void;
}

const ChatbotInterface = ({ onBack }: ChatbotInterfaceProps) => {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: '1',
      text: "Hello! I'm the ASD Assistant - your dedicated Autism Spectrum Disorder support chatbot. I'm here to help answer questions about autism, provide information, and offer support. How can I assist you today?",
      isUser: false,
      timestamp: new Date(),
      references: []
    }
  ]);
  const [inputText, setInputText] = useState("");
  const [isTyping, setIsTyping] = useState(false);
  const scrollAreaRef = useRef<HTMLDivElement>(null);

  // Sample responses for demonstration
  const sampleResponses = [
    {
      text: "Autism Spectrum Disorder (ASD) is a neurodevelopmental condition characterized by differences in social communication, interaction, and behavior patterns. It's called a 'spectrum' because it affects individuals very differently and to varying degrees.",
      references: ["DSM-5 Diagnostic Manual", "Autism Research Institute Guidelines"]
    },
    {
      text: "Early signs of autism in children may include delayed speech development, limited eye contact, repetitive behaviors, difficulty with social interactions, and intense interests in specific topics. It's important to consult with healthcare professionals for proper assessment.",
      references: ["Pediatric Development Guidelines", "Early Intervention Research"]
    },
    {
      text: "There are many evidence-based interventions for autism including Applied Behavior Analysis (ABA), speech therapy, occupational therapy, and social skills training. The best approach is individualized based on each person's unique needs and strengths.",
      references: ["Evidence-Based Practice Guidelines", "Autism Treatment Research"]
    }
  ];

  const handleSendMessage = async () => {
    if (!inputText.trim()) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      text: inputText,
      isUser: true,
      timestamp: new Date()
    };

    setMessages(prev => [...prev, userMessage]);
    setInputText("");
    setIsTyping(true);

    try {
      const response = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ query: inputText })
      });

      if (!response.ok) {
        throw new Error("Failed to fetch response from server");
      }

      const data = await response.json();

      const aiMessage: Message = {
        id: (Date.now() + 1).toString(),
        text: data.response,
        isUser: false,
        timestamp: new Date(),
        references: []
      };

      setMessages(prev => [...prev, aiMessage]);
    } catch (error) {
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        text: "Sorry, there was an error getting the response. Please try again.",
        isUser: false,
        timestamp: new Date(),
        references: []
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsTyping(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  useEffect(() => {
    if (scrollAreaRef.current) {
      scrollAreaRef.current.scrollTop = scrollAreaRef.current.scrollHeight;
    }
  }, [messages, isTyping]);

  const formatTime = (date: Date) => {
    return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-cyan-50">
      {/* Header */}
      <header className="bg-white/80 backdrop-blur-sm border-b border-blue-100 sticky top-0 z-50">
        <div className="container mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              <Button variant="ghost" onClick={onBack} className="hover:bg-blue-50">
                <ArrowLeft className="w-5 h-5 mr-2" />
                Back to Home
              </Button>
              <div className="h-6 w-px bg-gray-300"></div>
              <div className="flex items-center space-x-3">
                <div className="w-10 h-10 bg-gradient-to-r from-blue-500 to-cyan-600 rounded-lg flex items-center justify-center">
                  <Brain className="w-6 h-6 text-white" />
                </div>
                <div>
                  <h1 className="text-lg font-bold text-gray-900">ASD Assistant</h1>
                  <p className="text-sm text-gray-600">Autism Spectrum Disease Assistant</p>
                </div>
              </div>
            </div>
            <div className="flex items-center space-x-2">
              <Badge variant="secondary" className="bg-green-100 text-green-700">
                <div className="w-2 h-2 bg-green-500 rounded-full mr-2 animate-pulse"></div>
                Online
              </Badge>
              <Badge variant="secondary" className="bg-cyan-100 text-cyan-700">
                <Sparkles className="w-3 h-3 mr-1" />
                AI Powered
              </Badge>
            </div>
          </div>
        </div>
      </header>

      {/* Chat Container */}
      <div className="container mx-auto px-6 py-6 max-w-4xl">
        <Card className="h-[calc(100vh-200px)] flex flex-col shadow-xl border-blue-100">
          {/* Chat Messages */}
          <ScrollArea className="flex-1 p-6" ref={scrollAreaRef}>
            <div className="space-y-6">
              {messages.map((message) => (
                <div
                  key={message.id}
                  className={`flex ${message.isUser ? 'justify-end' : 'justify-start'}`}
                >
                  <div className={`flex items-start space-x-3 max-w-[80%] ${message.isUser ? 'flex-row-reverse space-x-reverse' : ''}`}>
                    {/* Avatar */}
                    <div className={`w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0 ${
                      message.isUser 
                        ? 'bg-gradient-to-r from-blue-500 to-blue-600' 
                        : 'bg-gradient-to-r from-cyan-500 to-cyan-600'
                    }`}>
                      {message.isUser ? <User className="w-4 h-4 text-white" /> : <Bot className="w-4 h-4 text-white" />}
                    </div>

                    {/* Message Bubble */}
                    <div className={`rounded-2xl px-4 py-3 ${
                      message.isUser
                        ? 'bg-gradient-to-r from-blue-500 to-blue-600 text-white'
                        : 'bg-white border border-cyan-100 text-gray-900 shadow-sm'
                    }`}>
                      <p className="text-sm leading-relaxed">{message.text}</p>
                      
                      {/* References */}
                      {message.references && message.references.length > 0 && (
                        <div className="mt-3 pt-3 border-t border-cyan-100">
                          <p className="text-xs text-gray-600 mb-2">References:</p>
                          <div className="space-y-1">
                            {message.references.map((ref, index) => (
                              <Badge key={index} variant="secondary" className="text-xs bg-cyan-50 text-cyan-700 mr-1">
                                {ref}
                              </Badge>
                            ))}
                          </div>
                        </div>
                      )}

                      {/* Timestamp */}
                      <div className={`flex items-center mt-2 text-xs ${
                        message.isUser ? 'text-blue-100' : 'text-gray-500'
                      }`}>
                        <Clock className="w-3 h-3 mr-1" />
                        {formatTime(message.timestamp)}
                      </div>
                    </div>
                  </div>
                </div>
              ))}

              {/* Typing Indicator */}
              {isTyping && (
                <div className="flex justify-start">
                  <div className="flex items-start space-x-3 max-w-[80%]">
                    <div className="w-8 h-8 rounded-full bg-gradient-to-r from-cyan-500 to-cyan-600 flex items-center justify-center flex-shrink-0">
                      <Bot className="w-4 h-4 text-white" />
                    </div>
                    <div className="bg-white border border-cyan-100 rounded-2xl px-4 py-3 shadow-sm">
                      <div className="flex space-x-1">
                        <div className="w-2 h-2 bg-cyan-400 rounded-full animate-bounce"></div>
                        <div className="w-2 h-2 bg-cyan-400 rounded-full animate-bounce" style={{ animationDelay: '0.1s' }}></div>
                        <div className="w-2 h-2 bg-cyan-400 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></div>
                      </div>
                    </div>
                  </div>
                </div>
              )}
            </div>
          </ScrollArea>

          {/* Input Area */}
          <CardContent className="border-t border-blue-100 p-6">
            <div className="flex space-x-3">
              <Input
                value={inputText}
                onChange={(e) => setInputText(e.target.value)}
                onKeyPress={handleKeyPress}
                placeholder="Ask me anything about autism..."
                className="flex-1 border-blue-200 focus:border-blue-500 focus:ring-blue-500"
                disabled={isTyping}
              />
              <Button
                onClick={handleSendMessage}
                disabled={!inputText.trim() || isTyping}
                className="bg-gradient-to-r from-blue-500 to-cyan-600 hover:from-blue-600 hover:to-cyan-700 px-6"
              >
                <Send className="w-4 h-4" />
              </Button>
            </div>
            <p className="text-xs text-gray-500 mt-2">
              Press Enter to send • This is a demo interface with sample responses
            </p>
          </CardContent>
        </Card>

        {/* Quick Actions */}
        <div className="mt-6">
          <h3 className="text-sm font-medium text-gray-700 mb-3">Quick Questions:</h3>
          <div className="flex flex-wrap gap-2">
            {[
              "What is autism?",
              "Early signs of autism",
              "Available treatments",
              "Support resources",
              "Research updates"
            ].map((question, index) => (
              <Button
                key={index}
                variant="outline"
                size="sm"
                onClick={() => setInputText(question)}
                className="border-cyan-200 text-cyan-700 hover:bg-cyan-50"
                disabled={isTyping}
              >
                {question}
              </Button>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default ChatbotInterface;
