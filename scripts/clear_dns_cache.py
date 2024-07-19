import os

def clear_dns_cache():
    """
    Clears the DNS cache using the ipconfig /flushdns command.
    """
    os.system("ipconfig /flushdns")  # Run the command to flush DNS cache
    print("DNS cache cleared successfully.")