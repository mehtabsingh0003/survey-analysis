# Use the official Node.js image from Docker Hub
FROM node:14

# Create a directory for the app inside the container
WORKDIR /usr/src/app

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the application code to the container
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Command to start the app
CMD ["node", "user-service.js"]
