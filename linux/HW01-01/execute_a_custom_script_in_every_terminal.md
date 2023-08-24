
#execute a custom script in every termina
Step2:
What is the alternative way to execute a custom script in every terminal? Try to create some examples and write down all the commands in a text file with good comment (absolute path / environment variables)

Custom Script Execution Instructions:

1. Create your custom script (e.g., my_script.sh):

   # my_script.sh
   echo "Hello from my custom script!"

2. Choose a location that's included in the system's PATH. For example, we'll use /usr/local/bin.

3. Copy your script to the chosen directory using superuser privileges:

   sudo cp my_script.sh /usr/local/bin/

4. Make the script executable:

   sudo chmod +x /usr/local/bin/my_script.sh

5. To use the script immediately in your current terminal session, run:

   source ~/.bashrc

   (Note: This step is not required for new terminal sessions.)

6. You can now execute your custom script from any terminal window:

   my_script.sh
