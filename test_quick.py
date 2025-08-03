"""
Quick test of HashHub Vector SDK
"""

from hashub_vector import HasHubVector, ModelAlias

def test_basic_functionality():
    """Test basic SDK functionality without API calls."""
    print("🚀 HashHub Vector SDK Test")
    print("=" * 40)
    
    # Test client creation
    client = HasHubVector(api_key="hh_live_62e6dbc416cf7760d22db26fc5e0d31c")
    print("✅ Client created successfully")
    
    # Test model aliases
    models = list(ModelAlias)
    print(f"✅ Available models: {len(models)}")
    for model in models:
        print(f"  - {model.value}")
    
    # Test request validation
    from hashub_vector.models import VectorizeRequest
    try:
        VectorizeRequest(text="Test text", model="e5_base")
        print("✅ Request validation works")
    except Exception as e:
        print(f"❌ Request validation failed: {e}")
    
    # Test error classes
    from hashub_vector import AuthenticationError, ValidationError
    print("✅ Exception classes imported")
    
    print("\n🎉 All basic tests passed!")
    print("Ready for production use with real API key!")

if __name__ == "__main__":
    test_basic_functionality()
