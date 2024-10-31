# Use the base image
FROM python:3.13

# Define build-time arguments
ARG OPENAI_API_KEY

# Create a new user
RUN useradd -ms /bin/bash erangalds
# Created User
RUN echo "Creating user completed" >> /project-code/debug.log
# Set environment variables
ENV OPENAI_API_KEY=${OPENAI_API_KEY} 
# Setting Environment Variables
RUN echo "Setting environment variables completed" >> /project-code/debug.log
# Switch to the new user
USER erangalds

# Set the working directory
WORKDIR /project-code
# Starting the Container
RUN echo "Starting container" >> /project-code/debug.log
# Entry point
CMD ["tail", "-f", "/dev/null"] 

