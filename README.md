# Cloud Computing Lab sessions
This repository contains all the lab sessions of MSC BirkBeck Cloud Computing course.

## Deploy to Google Cloud Platform VM

```bash
gcloud compute ssh --zone "your-zone" "your-vm-name" --project "your-project-id"
```

### Install Docker if it's not already installed on your VM

```bash
sudo apt-get update
sudo apt-get install docker.io
```

### Configure Docker to start on boot

```bash
sudo systemctl enable docker
sudo systemctl start docker
```

### Authenticate with the GitHub Container Registry

```bash
echo $GITHUB_PAT | docker login ghcr.io -u USERNAME --password-stdin
```

### Pull your Docker image

```bash
docker pull ghcr.io/your-username/your-repo-name:latest
```

### Run your Docker container

```bash
docker run -e DB_CONNECTOR='mongodb+srv://<username>:<password>@cluster0.55555.mongodb.net/myFirstDatabase?retryWrites=true&w=majority' -e TOKEN_SECRET='your-token-secret' -d -p 3000:3000 ghcr.io/your-username/your-repo-name:latest
```

### Create a script on your VM

```bash path=/home/user/deploy.sh mode=EDIT
#!/bin/bash

# Pull the latest image
docker pull ghcr.io/your-username/your-repo-name:latest

# Stop and remove the old container if it exists
docker stop my-app-container || true
docker rm my-app-container || true

# Run the new container
docker run -e DB_CONNECTOR='mongodb+srv://<username>:<password>@cluster0.55555.mongodb.net/myFirstDatabase?retryWrites=true&w=majority' -e TOKEN_SECRET='your-token-secret' -d --name my-app-container -p 3000:3000 ghcr.io/your-username/your-repo-name:latest
```

```bash
chmod +x /home/user/deploy.sh
```

### Automate the deployment

```yaml path=.github/workflows/docker-build-push.yml mode=EDIT
    - name: Deploy to Google Cloud VM
      env:
        PRIVATE_KEY: ${{ secrets.GCP_SSH_PRIVATE_KEY }}
        HOST: ${{ secrets.GCP_VM_IP }}
        USER: ${{ secrets.GCP_VM_USER }}
      run: |
        echo "$PRIVATE_KEY" > private_key && chmod 600 private_key
        ssh -o StrictHostKeyChecking=no -i private_key ${USER}@${HOST} '/home/user/deploy.sh'
```