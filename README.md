# claude_sonnet_cookbook

We choose to use GCP and VertexAI for exposing Anthropic Sonnet models. Examples 
are provided in both Node.js and Python

### Install gcloud
```
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
```

### Initialize the gcloud environment
```
gcloud init
gcloud components update
gcloud components install beta
gcloud auth application-default login
gcloud auth print-access-token
```

### Print environment information
```
export PROJECT_ID=`gcloud info --format=flattened | awk '/config.project/ {print $2}'`
gcloud compute project-info describe --project ${PROJECT_ID}
```

### Installs nvm (Node Version Manager) and Node.js
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash
nvm install 20
```

### Install Node.js dependencies
```
npm install @google-cloud/vertexai
npm install @google-cloud/storage
npm install @anthropic-ai/vertex-sdk
```
### Install Python dependencies for Anthropic
```
python -m pip install -U 'anthropic[vertex]'
```

python -m pip install -U 'anthropic[vertex]'
