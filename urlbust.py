"""
Created by GTekSD
"""
import webbrowser
import sys
import time

def open_urls_in_batches(filename, batch_size):
    try:
        with open(filename, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]

        total_urls = len(urls)
        batch_count = (total_urls + batch_size - 1) // batch_size  # Calculate total batches

        for i in range(batch_count):
            print(f"\nOpening batch {i + 1} of {batch_count}...")

            # Open current batch of URLs
            for url in urls[i * batch_size: (i + 1) * batch_size]:
                print(f"Opening: {url}")
                webbrowser.open(url)
                time.sleep(1)  # Optional: Add delay to avoid overwhelming the browser

            # Wait for user confirmation to proceed to the next batch
            if i < batch_count - 1:
                input("\nPress Enter to open the next batch (or CTRL+C to exit)...")

        print("\nAll URLs opened.")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting...")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python scrypt.py <batch_size> <url_file>")
    else:
        try:
            batch_size = int(sys.argv[1])
            filename = sys.argv[2]
            open_urls_in_batches(filename, batch_size)
        except ValueError:
            print("Error: Batch size must be an integer.")
