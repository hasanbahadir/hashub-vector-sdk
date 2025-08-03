"""
Hashub Vector SDK Live Test
Test with real API calls using the Hashub Vector API
"""

import os
import asyncio
from hashub_vector import HashubVector

# Real API key for testing
API_KEY = "hh_live_62e6dbc416cf7760d22db26fc5e0d31c"

def test_turkish_optimization():
    """Test Turkish language optimization with real API calls."""
    print("🇹🇷 Hashub Vector SDK - Turkish Language Test")
    print("=" * 60)
    
    # Create client with real API key (base_url is optional, defaults to production)
    client = HashubVector(api_key=API_KEY)
    print("✅ Client created with live API key")
    
    try:
        # Test Turkish text with best model for Turkish
        turkish_text = "Hashub Vector API ile Türkçe metinlerinizi güçlü vektörlere dönüştürün!"
        print(f"\n📝 Turkish Text: {turkish_text}")
        
        response = client.vectorize(turkish_text, model="gte_base")  # Best for Turkish
        
        print(f"✅ Vectorization successful!")
        print(f"📊 Model: {response.model}")
        print(f"📊 Dimension: {response.dimension}")
        print(f"📊 Token count: {response.token_count}")
        print(f"📊 Processing time: {response.processing_time_ms}ms")
        print(f"📊 Vector magnitude: {response.magnitude:.4f}")
        print(f"📊 First 5 dimensions: {response.vector[:5]}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    finally:
        client.close()

def test_multilingual_batch():
    """Test multilingual batch processing."""
    print("\n🌍 Multilingual Batch Processing Test")
    print("-" * 50)
    
    client = HashubVector(
        api_key=API_KEY,
        base_url="https://vector.hashub.dev"
    )
    
    try:
        # Multilingual texts
        texts = [
            "Hello world! This is English text.",
            "Merhaba dünya! Bu Türkçe bir metindir.",
            "Bonjour le monde! Ceci est un texte français.",
            "¡Hola mundo! Este es un texto en español.",
            "Hallo Welt! Das ist ein deutscher Text."
        ]
        
        print(f"📦 Processing {len(texts)} multilingual texts...")
        
        response = client.vectorize_batch(texts, model="gte_base")
        
        print(f"✅ Batch processing successful!")
        print(f"📊 Model: {response.model}")
        print(f"📊 Total vectors: {response.count}")
        print(f"📊 Total tokens: {response.total_tokens}")
        print(f"📊 Average tokens per text: {response.total_tokens / response.count:.1f}")
        print(f"📊 Processing time: {response.processing_time_ms}ms")
        
        # Show details for each text
        languages = ["English", "Turkish", "French", "Spanish", "German"]
        for i, (text, lang, tokens) in enumerate(zip(texts, languages, response.token_counts)):
            print(f"  {i+1}. {lang}: {tokens} tokens")
            print(f"     Text: {text[:40]}...")
            print(f"     Vector preview: {response.vectors[i][:3]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    finally:
        client.close()

def test_similarity_calculation():
    """Test similarity calculation between Turkish and English."""
    print("\n🔍 Cross-lingual Similarity Test")
    print("-" * 40)
    
    client = HashubVector(
        api_key=API_KEY,
        base_url="https://vector.hashub.dev"
    )
    
    try:
        # Test similarity between Turkish and English equivalents
        test_pairs = [
            ("Machine learning", "Makine öğrenmesi"),
            ("Artificial intelligence", "Yapay zeka"),
            ("Deep learning", "Derin öğrenme"),
            ("Data science", "Veri bilimi"),
            ("Natural language processing", "Doğal dil işleme")
        ]
        
        print(f"{'English':<30} {'Turkish':<25} {'Similarity':<12}")
        print("-" * 70)
        
        for english, turkish in test_pairs:
            similarity = client.similarity(english, turkish, model="gte_base")
            print(f"{english:<30} {turkish:<25} {similarity:<12.3f}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    finally:
        client.close()

def test_model_comparison():
    """Test the same Turkish text with different models."""
    print("\n⚖️ Model Comparison Test")
    print("-" * 35)
    
    client = HashubVector(
        api_key=API_KEY,
        base_url="https://vector.hashub.dev"
    )
    
    try:
        turkish_text = "Yapay zeka teknolojisi günümüzde hızla gelişmektedir."
        models = ["e5_small", "e5_base", "mpnet_base", "gte_base"]
        
        print(f"Turkish text: {turkish_text}")
        print(f"\n{'Model':<15} {'Dimension':<10} {'Tokens':<8} {'Time (ms)':<12} {'Magnitude':<10}")
        print("-" * 70)
        
        for model in models:
            response = client.vectorize(turkish_text, model=model)
            print(f"{model:<15} {response.dimension:<10} {response.token_count:<8} {response.processing_time_ms or 0:<12.1f} {response.magnitude:<10.4f}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    finally:
        client.close()

async def test_async_operations():
    """Test asynchronous operations."""
    print("\n⚡ Async Operations Test")
    print("-" * 30)
    
    async with HashubVector(api_key=API_KEY) as client:
        try:
            # Async single embedding
            turkish_text = "Asenkron işlemler ile hızlı embedding!"
            response = await client.avectorize(turkish_text, model="e5_base")
            print(f"✅ Async single embedding: {response.dimension}d vector, {response.token_count} tokens")
            
            # Async batch processing
            texts = [
                "Fast async processing",
                "Hızlı asenkron işleme", 
                "Traitement asynchrone rapide"
            ]
            batch_response = await client.avectorize_batch(texts, model="e5_base")
            print(f"✅ Async batch processing: {batch_response.count} vectors, {batch_response.total_tokens} total tokens")
            
            return True
            
        except Exception as e:
            print(f"❌ Async error: {e}")
            return False

def test_usage_monitoring():
    """Test usage monitoring."""
    print("\n📊 Usage Monitoring Test")
    print("-" * 30)
    
    client = HashubVector(
        api_key=API_KEY,
        base_url="https://vector.hashub.dev"
    )
    
    try:
        usage = client.get_usage()
        print(f"✅ Usage information retrieved:")
        print(f"📊 Tokens used: {usage.tokens_used:,}")
        
        if usage.tokens_remaining:
            print(f"📊 Tokens remaining: {usage.tokens_remaining:,}")
            print(f"📊 Usage percentage: {usage.tokens_percentage_used:.1f}%")
        
        if usage.requests_used:
            print(f"📊 Requests made: {usage.requests_used}")
        
        return True
        
    except Exception as e:
        print(f"❌ Usage monitoring error: {e}")
        return False
    
    finally:
        client.close()

def test_error_handling():
    """Test error handling with invalid inputs."""
    print("\n⚠️ Error Handling Test")
    print("-" * 25)
    
    client = HashubVector(
        api_key=API_KEY,
        base_url="https://vector.hashub.dev"
    )
    
    try:
        # Test invalid model
        try:
            client.vectorize("Test", model="invalid_model")
            print("❌ Should have raised ModelNotFoundError")
            return False
        except Exception as e:
            print(f"✅ Correctly caught error for invalid model: {type(e).__name__}")
        
        # Test empty text
        try:
            client.vectorize("")
            print("❌ Should have raised ValidationError")
            return False
        except ValueError as e:
            print(f"✅ Correctly caught error for empty text: {type(e).__name__}")
        
        print("✅ Error handling works correctly")
        return True
        
    except Exception as e:
        print(f"❌ Unexpected error in error handling test: {e}")
        return False
    
    finally:
        client.close()

def main():
    """Run all live tests."""
    print("🚀 Hashub Vector SDK - Live API Tests")
    print("=" * 80)
    print(f"🔑 Using API Key: {API_KEY[:20]}...")
    print()
    
    test_results = []
    
    # Run synchronous tests
    test_results.append(("Turkish Optimization", test_turkish_optimization()))
    test_results.append(("Multilingual Batch", test_multilingual_batch()))
    test_results.append(("Similarity Calculation", test_similarity_calculation()))
    test_results.append(("Model Comparison", test_model_comparison()))
    test_results.append(("Usage Monitoring", test_usage_monitoring()))
    test_results.append(("Error Handling", test_error_handling()))
    
    # Run async test
    print("Running async tests...")
    async_result = asyncio.run(test_async_operations())
    test_results.append(("Async Operations", async_result))
    
    # Print summary
    print("\n" + "=" * 80)
    print("📋 TEST SUMMARY")
    print("=" * 80)
    
    passed = 0
    total = len(test_results)
    
    for test_name, result in test_results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name:<25} {status}")
        if result:
            passed += 1
    
    print(f"\n🎯 Overall Result: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Hashub Vector SDK is working perfectly!")
    else:
        print("⚠️ Some tests failed. Please check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
