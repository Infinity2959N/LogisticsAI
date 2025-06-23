# 🚀 LogisticsAI Setup Guide

This guide will help you set up the LogisticsAI project for development, testing, or deployment. Follow the steps appropriate for your use case.

## 📋 Table of Contents

- [Quick Start](#quick-start)
- [Detailed Setup](#detailed-setup)
- [Development Environment](#development-environment)
- [Testing Setup](#testing-setup)
- [Production Deployment](#production-deployment)
- [Troubleshooting](#troubleshooting)

## ⚡ Quick Start

For the impatient developer who wants to get started immediately:

```bash
# 1. Clone and navigate
git clone https://github.com/Infinity2959N/LogisticsAI.git
cd LogisticsAI

# 2. Set up Python environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Set up Flutter app
cd "Flutter App"
flutter pub get
echo "GOOGLE_MAPS_API_KEY=your_key_here" > .env

# 4. Test algorithms
cd "../Algorithm Testing"
python data_gen.py
python output_eval.py

# 5. Run Flutter app
cd "../Flutter App"
flutter run
```

## 🔧 Detailed Setup

### Prerequisites Checklist

Before starting, ensure you have:

- [ ] **Git** (2.30+) - Version control
- [ ] **Python** (3.8+) - Algorithm development
- [ ] **Flutter SDK** (3.0+) - Mobile app development
- [ ] **Google Maps API Key** - Real-world routing
- [ ] **Code Editor** (VS Code recommended)

#### Installing Prerequisites

<details>
<summary>🐍 Python Installation</summary>

**Windows:**
```powershell
# Using winget
winget install Python.Python.3.11

# Or download from python.org
# https://www.python.org/downloads/windows/
```

**macOS:**
```bash
# Using Homebrew
brew install python@3.11

# Using pyenv (recommended)
pyenv install 3.11.0
pyenv global 3.11.0
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip
```

</details>

<details>
<summary>📱 Flutter Installation</summary>

**All Platforms:**
1. Download Flutter SDK from [flutter.dev](https://flutter.dev/docs/get-started/install)
2. Extract to your preferred location
3. Add Flutter to PATH:

**Windows:**
```powershell
# Add to PATH in Environment Variables
C:\path\to\flutter\bin
```

**macOS/Linux:**
```bash
# Add to ~/.bashrc or ~/.zshrc
export PATH="$PATH:/path/to/flutter/bin"
source ~/.bashrc  # or ~/.zshrc
```

4. Verify installation:
```bash
flutter doctor
```

</details>

<details>
<summary>🗺️ Google Maps API Key</summary>

1. **Go to Google Cloud Console**: [console.cloud.google.com](https://console.cloud.google.com)
2. **Create/Select Project**: Create new or select existing project
3. **Enable APIs**:
   - Distance Matrix API
   - Geocoding API
   - Maps SDK for Android
   - Maps SDK for iOS
4. **Create Credentials**: Go to "Credentials" → "Create Credentials" → "API Key"
5. **Secure Key**: Restrict key to your domains/apps
6. **Note Key**: Save for configuration

</details>

### Repository Setup

1. **Clone Repository**
   ```bash
   git clone https://github.com/Infinity2959N/LogisticsAI.git
   cd LogisticsAI
   ```

2. **Verify Structure**
   ```bash
   ls -la
   # Should show: algos/, Algorithm Testing/, Final python pipeline/, Flutter App/
   ```

### Python Environment Setup

1. **Create Virtual Environment**
   ```bash
   python -m venv venv
   
   # Activate (choose one):
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate         # Windows CMD
   venv\Scripts\Activate.ps1     # Windows PowerShell
   ```

2. **Upgrade pip**
   ```bash
   python -m pip install --upgrade pip
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Installation**
   ```bash
   python -c "import numpy, pandas, matplotlib; print('All packages installed successfully!')"
   ```

### Flutter Environment Setup

1. **Navigate to Flutter App**
   ```bash
   cd "Flutter App"
   ```

2. **Install Dependencies**
   ```bash
   flutter pub get
   ```

3. **Configure Environment**
   ```bash
   # Create .env file
   echo "GOOGLE_MAPS_API_KEY=your_actual_api_key_here" > .env
   
   # On Windows PowerShell:
   # "GOOGLE_MAPS_API_KEY=your_actual_api_key_here" | Out-File -FilePath .env -Encoding UTF8
   ```

4. **Verify Setup**
   ```bash
   flutter doctor
   flutter analyze
   ```

## 💻 Development Environment

### IDE Setup

#### Visual Studio Code (Recommended)

1. **Install Extensions**:
   ```bash
   code --install-extension ms-python.python
   code --install-extension dart-code.flutter
   code --install-extension dart-code.dart-code
   code --install-extension ms-python.pylint
   code --install-extension ms-python.black-formatter
   ```

2. **Configure Settings** (`.vscode/settings.json`):
   ```json
   {
     "python.defaultInterpreterPath": "./venv/bin/python",
     "python.formatting.provider": "black",
     "python.linting.enabled": true,
     "python.linting.pylintEnabled": true,
     "dart.flutterSdkPath": "/path/to/flutter",
     "editor.formatOnSave": true
   }
   ```

#### PyCharm/IntelliJ Setup

1. **Configure Python Interpreter**: Point to `venv/bin/python`
2. **Install Dart/Flutter Plugins**: From plugin marketplace
3. **Configure Formatter**: Set Black as Python formatter

### Development Workflow

1. **Start Development Session**
   ```bash
   # Activate Python environment
   source venv/bin/activate
   
   # Start Jupyter for algorithm analysis
   jupyter lab
   
   # In another terminal, start Flutter
   cd "Flutter App"
   flutter run
   ```

2. **Code Quality Checks**
   ```bash
   # Python formatting
   black algos/ "Algorithm Testing/" "Final python pipeline/"
   
   # Python linting
   flake8 algos/
   
   # Flutter analysis
   cd "Flutter App"
   flutter analyze
   dart format lib/
   ```

## 🧪 Testing Setup

### Algorithm Testing

1. **Generate Test Data**
   ```bash
   cd "Algorithm Testing"
   python data_gen.py
   ```

2. **Run Algorithm Benchmarks**
   ```bash
   python output_eval.py
   ```

3. **View Analysis**
   ```bash
   jupyter notebook "Benchmark/Benchmark Analysis and EDA.ipynb"
   ```

### Flutter Testing

1. **Unit Tests**
   ```bash
   cd "Flutter App"
   flutter test
   ```

2. **Integration Tests**
   ```bash
   flutter test integration_test/
   ```

3. **Widget Tests**
   ```bash
   flutter test --coverage
   genhtml coverage/lcov.info -o coverage/html
   ```

### Python Testing

1. **Unit Tests**
   ```bash
   cd algos
   python -m pytest tests/ -v
   ```

2. **Coverage Report**
   ```bash
   python -m pytest --cov=algos --cov-report=html
   ```

## 🚀 Production Deployment

### Backend Deployment

1. **Prepare Environment**
   ```bash
   pip install gunicorn flask flask-cors
   ```

2. **Create Production App**
   ```python
   # app.py
   from flask import Flask, request, jsonify
   from path_optimizer import optimize_route_api
   
   app = Flask(__name__)
   
   @app.route('/optimize', methods=['POST'])
   def optimize():
       data = request.get_json()
       result = optimize_route_api(data['locations'], data['api_key'])
       return jsonify(result)
   
   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)
   ```

3. **Deploy with Gunicorn**
   ```bash
   gunicorn --bind 0.0.0.0:5000 app:app
   ```

### Mobile App Deployment

#### Android

1. **Build APK**
   ```bash
   cd "Flutter App"
   flutter build apk --release
   ```

2. **Build App Bundle**
   ```bash
   flutter build appbundle --release
   ```

#### iOS

1. **Build for iOS**
   ```bash
   flutter build ios --release
   ```

2. **Archive in Xcode**
   - Open `ios/Runner.xcworkspace` in Xcode
   - Product → Archive

### Docker Deployment

1. **Create Dockerfile**
   ```dockerfile
   FROM python:3.11-slim
   
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   
   COPY . .
   EXPOSE 5000
   
   CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
   ```

2. **Build and Run**
   ```bash
   docker build -t logistics-ai .
   docker run -p 5000:5000 -e GOOGLE_MAPS_API_KEY=your_key logistics-ai
   ```

## 🔧 Configuration

### Environment Variables

Create `.env` files for different components:

#### Python Backend (`.env`)
```bash
GOOGLE_MAPS_API_KEY=your_google_maps_api_key
FLASK_ENV=development
LOG_LEVEL=INFO
REDIS_URL=redis://localhost:6379
DATABASE_URL=postgresql://user:pass@localhost/logistics
```

#### Flutter App (`Flutter App/.env`)
```bash
GOOGLE_MAPS_API_KEY=your_google_maps_api_key
API_BASE_URL=http://localhost:5000
ENVIRONMENT=development
```

### Algorithm Parameters

Customize algorithm behavior in `config.py`:

```python
# config.py
ALGORITHM_PARAMS = {
    "aco": {
        "alpha": 1.0,
        "beta": 2.0,
        "rho": 0.1,
        "num_ants": 20,
        "iterations": 100
    },
    "genetic": {
        "population_size": 50,
        "generations": 100,
        "mutation_rate": 0.02,
        "elite_size": 20
    }
}
```

## 🔍 Troubleshooting

### Common Issues

<details>
<summary>🐍 Python Issues</summary>

**Issue**: `ModuleNotFoundError: No module named 'numpy'`
**Solution**:
```bash
# Ensure virtual environment is activated
source venv/bin/activate
pip install -r requirements.txt
```

**Issue**: `Permission denied` when installing packages
**Solution**:
```bash
# Use virtual environment instead of system Python
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

</details>

<details>
<summary>📱 Flutter Issues</summary>

**Issue**: `Flutter command not found`
**Solution**:
```bash
# Add Flutter to PATH
export PATH="$PATH:/path/to/flutter/bin"
# Or restart terminal after installation
```

**Issue**: `Android license status unknown`
**Solution**:
```bash
flutter doctor --android-licenses
# Accept all licenses
```

**Issue**: `CocoaPods not installed` (iOS)
**Solution**:
```bash
sudo gem install cocoapods
cd "Flutter App/ios"
pod install
```

</details>

<details>
<summary>🗺️ Google Maps Issues</summary>

**Issue**: `API key not valid`
**Solution**:
1. Check API key in Google Cloud Console
2. Ensure required APIs are enabled
3. Check API key restrictions
4. Verify billing is enabled

**Issue**: `OVER_QUERY_LIMIT` error
**Solution**:
1. Check API quotas in Google Cloud Console
2. Implement request throttling
3. Consider upgrading billing plan

</details>

<details>
<summary>💻 Development Issues</summary>

**Issue**: Jupyter notebooks not starting
**Solution**:
```bash
# Ensure Jupyter is installed in virtual environment
pip install jupyter
jupyter notebook --generate-config
```

**Issue**: Import errors in Python modules
**Solution**:
```bash
# Ensure you're in the correct directory
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

</details>

### Performance Optimization

1. **Algorithm Performance**
   ```python
   # Reduce problem size for faster testing
   SMALL_TEST_PARAMS = {
       "iterations": 50,
       "num_ants": 10
   }
   ```

2. **API Performance**
   ```python
   # Implement caching for repeated requests
   import functools
   
   @functools.lru_cache(maxsize=128)
   def cached_distance_calculation(origin, destination):
       # Implementation
   ```

3. **Flutter Performance**
   ```bash
   # Build in release mode for testing
   flutter run --release
   ```

## 📞 Getting Help

If you encounter issues not covered here:

1. **Check Documentation**: Review component-specific READMEs
2. **Search Issues**: Look through GitHub issues
3. **Create Issue**: Open new issue with:
   - Operating system
   - Python/Flutter versions
   - Error messages
   - Steps to reproduce

## ✅ Verification Checklist

Before starting development, verify:

- [ ] Python virtual environment activated
- [ ] All Python packages installed successfully
- [ ] Flutter doctor shows no critical issues
- [ ] Google Maps API key configured
- [ ] Test data generation works
- [ ] Sample algorithm runs successfully
- [ ] Flutter app builds without errors
- [ ] Basic tests pass

---

**🎉 Congratulations!** You now have LogisticsAI set up and ready for development. Happy coding!
