#!/bin/bash

# Set the Webex bot access token and the user ID to send the message
ACCESS_TOKEN="ZDc5OGY5N2MtNGM2Ni00ZTMxLWI4YWItNTQzMGNlYTIwZDE4NzVmMjUzNTUtYTdl_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
USER_ID="taiahmed@cisco.webex.com"

# Path to the sshd log file
SSH_LOG="/var/log/auth.log"

# Monitor the sshd log file for login events
tail -fn0 "$SSH_LOG" | while read -r line; do
  if [[ $line == *"sshd"*"Accepted"* ]]; then
    # SSH login detected, send a 1:1 message via Webex API
    curl -X POST -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -d "{\"toPersonEmail\": \"$USER_ID\", \"text\": \"SSH login detected: $line\"}" "https://api.ciscospark.com/v1/messages"
  fi
done

