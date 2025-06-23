# 🔄 Python Backend Pipeline

This directory contains the production-ready backend pipeline that integrates Google Maps Distance Matrix API with our optimization algorithms to provide real-world route optimization capabilities.

## 📁 Directory Structure

```
Final python pipeline vizualization/
├── 🌐 api_ip_part.py                  # API input processing module
├── 📤 api_op_part.py                  # API output formatting module
├── 🐜 elist_ant_system.py            # Elitist ACO implementation
├── 🗺️ path_optimizer.py              # Main optimization logic
└── 📍 locations.txt                  # Sample location data
```

## 🏗️ Pipeline Architecture

The backend pipeline follows a modular architecture designed for scalability and maintainability:

```
Input Locations → API Processing → Distance Matrix → Algorithm Optimization → Formatted Output
```

### Data Flow
1. **Input Processing**: Parse location strings/coordinates
2. **API Integration**: Fetch real-world distances via Google Maps
3. **Matrix Construction**: Build symmetric distance/time matrix
4. **Route Optimization**: Apply ACO algorithm for optimal routing
5. **Output Formatting**: Return mobile-app compatible results

## 🌐 API Integration Layer

### Google Maps Distance Matrix API

Our pipeline integrates with Google's Distance Matrix API to provide:
- **Real-world Distances**: Actual driving distances, not Euclidean
- **Traffic Awareness**: Current traffic conditions in calculations
- **Multiple Transportation Modes**: Driving, walking, transit options
- **Accurate Time Estimates**: Dynamic travel time predictions

### API Configuration
```python
GOOGLE_MAPS_API_BASE_URL = "https://maps.googleapis.com/maps/api/distancematrix/json"

# Request parameters
params = {
    "origins": "location1",
    "destinations": "location2", 
    "key": api_key,
    "mode": "driving",           # driving, walking, bicycling, transit
    "units": "metric",           # metric or imperial
    "avoid": "tolls"             # Optional: tolls, highways, ferries
}
```

## 🗺️ Path Optimizer (Core Module)

**File**: `path_optimizer.py`

The main optimization engine that coordinates API calls and algorithm execution.

### Key Functions

#### `get_time_matrix(locations, api_key)`
Constructs the distance/time matrix using Google Maps API.

**Parameters:**
- `locations`: List of location strings (addresses, coordinates, place names)
- `api_key`: Google Maps API key

**Returns:**
- 2D matrix with travel times in seconds between all location pairs

**Features:**
- **Batch Processing**: Optimizes API calls to minimize costs
- **Error Handling**: Robust handling of API failures and invalid locations
- **Rate Limiting**: Respects Google's API rate limits
- **Caching**: Optional result caching for repeated requests

```python
# Example usage
locations = [
    "New Delhi Railway Station, Delhi",
    "Mumbai Central Station, Mumbai", 
    "Kolkata Railway Station, Kolkata",
    "Chennai Central Station, Chennai"
]

matrix = get_time_matrix(locations, your_api_key)
# Returns: [[0, 1200, 1800, 2100], [1200, 0, 2000, 1300], ...]
```

#### `optimize_route(matrix, start_location)`
Applies the Elitist ACO algorithm to find optimal route.

**Parameters:**
- `matrix`: Distance/time matrix from Google Maps
- `start_location`: Index of starting location (warehouse)

**Returns:**
- Optimized route with total cost and detailed path

### Algorithm Integration

The pipeline uses our **Elitist ACO** algorithm as the primary optimizer due to its:
- **Superior Solution Quality**: Consistently finds high-quality routes
- **Reasonable Runtime**: Fast enough for real-time applications  
- **Stability**: Reliable convergence across different problem sizes
- **Real-world Validation**: Proven performance on actual logistics data

### Error Handling & Resilience

```python
def robust_api_call(origin, destination, api_key, max_retries=3):
    """
    Robust API call with exponential backoff retry logic
    """
    for attempt in range(max_retries):
        try:
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                return process_response(response.json())
        except RequestException as e:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                raise e
```

## 🐜 Elitist Ant Colony System

**File**: `elist_ant_system.py`

Production-optimized implementation of the Elitist ACO algorithm specifically tuned for real-world logistics applications.

### Production Optimizations

#### Performance Enhancements
- **Vectorized Operations**: NumPy-based matrix operations
- **Memory Efficiency**: Optimized data structures for large problems
- **Early Termination**: Convergence detection to avoid unnecessary iterations
- **Parallel Ant Construction**: Multi-threaded ant tour construction

#### Parameter Tuning for Real-world Data
```python
production_params = {
    "alpha": 1.0,           # Balanced pheromone influence
    "beta": 2.5,            # Emphasize short distances for logistics
    "rho": 0.1,             # Moderate evaporation for stability
    "num_ants": min(25, n), # Scale ants with problem size
    "iterations": 150,      # Higher iterations for quality
    "elite_weight": 3.0,    # Strong elite reinforcement
    "convergence_check": 20 # Stop if no improvement for 20 iterations
}
```

#### Real-world Adaptations
- **Asymmetric Matrix Handling**: Support for non-symmetric travel times
- **Time Window Constraints**: Optional delivery time window support
- **Vehicle Capacity**: Extensions for capacity-constrained routing
- **Dynamic Updates**: Support for real-time traffic updates

## 📤 API Output Formatting

**File**: `api_op_part.py`

Formats optimization results for consumption by the Flutter mobile application.

### Output Format
```json
{
  "status": "success",
  "route": {
    "path": [0, 3, 1, 4, 2, 0],
    "locations": [
      {"index": 0, "name": "Warehouse", "address": "..."},
      {"index": 3, "name": "Delivery Point A", "address": "..."},
      ...
    ],
    "total_time": 7200,
    "total_distance": 245.7,
    "segments": [
      {
        "from": {"index": 0, "name": "Warehouse"},
        "to": {"index": 3, "name": "Delivery Point A"},
        "duration": 1800,
        "distance": 45.2,
        "google_maps_url": "https://maps.google.com/..."
      },
      ...
    ]
  },
  "optimization_info": {
    "algorithm": "elitist_aco",
    "iterations": 89,
    "improvement": 23.5,
    "computation_time": 2.4
  }
}
```

### Mobile App Integration Features
- **Google Maps URLs**: Direct navigation links for each route segment
- **Human-readable Addresses**: Formatted location names and addresses
- **Progress Tracking**: Completion status for each delivery
- **Route Visualization**: Coordinates for map rendering
- **Performance Metrics**: Algorithm performance information

## 📍 Sample Data

**File**: `locations.txt`

Contains sample location data for testing the pipeline with Indian cities and addresses.

### Format Examples
```
# Major Indian Cities
Mumbai, Maharashtra, India
Delhi, India  
Bangalore, Karnataka, India
Chennai, Tamil Nadu, India
Kolkata, West Bengal, India

# Specific Addresses
Connaught Place, New Delhi, Delhi, India
Marine Drive, Mumbai, Maharashtra, India
Brigade Road, Bangalore, Karnataka, India

# Coordinates (lat,lng format)
28.6139,77.2090  # New Delhi
19.0760,72.8777  # Mumbai
```

## 🚀 Quick Start Guide

### Prerequisites
```bash
pip install requests numpy pandas googlemaps
```

### Basic Usage
```python
from path_optimizer import get_time_matrix, optimize_route
from api_op_part import format_output

# 1. Define locations
locations = [
    "Warehouse, Industrial Area, Gurgaon",
    "Connaught Place, Delhi", 
    "Karol Bagh, Delhi",
    "Lajpat Nagar, Delhi"
]

# 2. Get Google Maps distance matrix  
api_key = "your_google_maps_api_key"
matrix = get_time_matrix(locations, api_key)

# 3. Optimize route
optimized_route = optimize_route(matrix, start_location=0)

# 4. Format for mobile app
formatted_output = format_output(optimized_route, locations)

print(f"Optimal route: {optimized_route['path']}")
print(f"Total time: {optimized_route['cost']} seconds")
```

### Production Deployment
```python
import os
from flask import Flask, request, jsonify
from path_optimizer import optimize_logistics_route

app = Flask(__name__)

@app.route('/optimize-route', methods=['POST'])
def optimize_route_endpoint():
    try:
        data = request.get_json()
        locations = data['locations']
        api_key = os.getenv('GOOGLE_MAPS_API_KEY')
        
        result = optimize_logistics_route(locations, api_key)
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## ⚡ Performance Optimization

### API Cost Optimization
- **Request Batching**: Minimize API calls through efficient batching
- **Result Caching**: Cache distance matrices for repeated location sets
- **Fallback Strategies**: Use cached data when API is unavailable
- **Smart Routing**: Avoid unnecessary API calls for known routes

### Algorithm Performance
- **Adaptive Parameters**: Adjust algorithm parameters based on problem size
- **Early Termination**: Stop optimization when convergence is detected
- **Parallel Processing**: Multi-threaded ant construction
- **Memory Management**: Efficient memory usage for large problem instances

### Production Considerations
```python
# Configuration for production environment
PRODUCTION_CONFIG = {
    "max_locations": 50,           # Limit problem size
    "api_timeout": 10,             # Request timeout in seconds
    "max_retries": 3,              # API retry attempts
    "cache_ttl": 3600,             # Cache time-to-live (1 hour)
    "algorithm_timeout": 30,        # Max optimization time
    "rate_limit": 1000,            # Requests per hour limit
}
```

## 🔧 Configuration & Environment

### Environment Variables
```bash
# Required
GOOGLE_MAPS_API_KEY=your_api_key_here

# Optional
CACHE_REDIS_URL=redis://localhost:6379
LOG_LEVEL=INFO
MAX_CONCURRENT_REQUESTS=5
API_RATE_LIMIT=1000
```

### Google Maps API Setup
1. **Enable APIs**: Distance Matrix API, Geocoding API
2. **Set Quotas**: Configure daily/monthly usage limits
3. **Restrict Key**: Limit API key to specific domains/IPs
4. **Monitor Usage**: Set up billing alerts and monitoring

## 📊 Testing & Validation

### Unit Tests
```python
def test_distance_matrix_construction():
    """Test Google Maps API integration"""
    locations = ["Delhi", "Mumbai", "Bangalore"]
    matrix = get_time_matrix(locations, test_api_key)
    
    assert len(matrix) == 3
    assert matrix[0][0] == 0  # Same location distance
    assert matrix[0][1] > 0   # Different location distance

def test_route_optimization():
    """Test ACO algorithm integration"""
    test_matrix = [[0, 10, 15], [10, 0, 20], [15, 20, 0]]
    result = optimize_route(test_matrix, 0)
    
    assert 'path' in result
    assert 'cost' in result
    assert result['path'][0] == 0  # Starts at warehouse
```

### Integration Tests
- **End-to-end Pipeline**: Full workflow from locations to optimized route
- **API Error Handling**: Network failures, invalid locations, quota limits
- **Algorithm Validation**: Verify optimization quality on known problems
- **Performance Benchmarks**: Runtime and memory usage validation

## 🔗 Integration Points

### Flutter App Integration
The pipeline is designed to integrate seamlessly with the Flutter mobile application:

```dart
// Flutter service call
Future<RouteOptimizationResult> optimizeRoute(List<String> locations) async {
  final response = await http.post(
    Uri.parse('$baseUrl/optimize-route'),
    headers: {'Content-Type': 'application/json'},
    body: jsonEncode({'locations': locations}),
  );
  
  return RouteOptimizationResult.fromJson(jsonDecode(response.body));
}
```

### External System Integration
- **REST API**: HTTP endpoints for route optimization requests
- **Webhook Support**: Notifications for route optimization completion
- **Database Integration**: Store and retrieve historical routes
- **Message Queue**: Asynchronous processing for large requests

## 📚 Further Reading

- **Google Maps API Documentation**: [Distance Matrix API Guide](https://developers.google.com/maps/documentation/distance-matrix)
- **ACO Algorithm Theory**: Dorigo, M., & Stützle, T. (2004). Ant Colony Optimization
- **Production Deployment**: Best practices for ML/optimization API deployment
- **Performance Optimization**: Techniques for high-throughput route optimization

## 👨‍💻 Author

**Bhavesh (B Infinity)**
- GitHub: [@Infinity2959N](https://github.com/Infinity2959N)
- Email: [binfinity321@gmail.com](mailto:binfinity321@gmail.com)

---

**Note**: This pipeline is production-ready and has been tested with real Indian logistics data. For deployment, ensure proper API key management, monitoring, and error handling are in place.
