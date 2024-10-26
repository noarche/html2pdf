import os
import pdfkit
import colorama
from colorama import Fore, Style
from tqdm import tqdm
from datetime import datetime

colorama.init(autoreset=True)

# Explicitly specify the path to wkhtmltopdf binary
path_to_wkhtmltopdf = r'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'  # Change this if necessary
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

def convert_html_to_pdf(html_file, output_file):
    """Convert a single HTML file to PDF."""
    try:
        pdfkit.from_file(html_file, output_file, configuration=config)
        return os.path.getsize(output_file)
    except Exception as e:
        print(f"{Fore.RED}Failed to convert {html_file}: {e}")
        return 0

def format_size(size_in_bytes):
    """Convert bytes to KB, MB, GB, or TB."""
    size_units = ['B', 'KB', 'MB', 'GB', 'TB']
    i = 0
    while size_in_bytes >= 1024 and i < len(size_units) - 1:
        size_in_bytes /= 1024.0
        i += 1
    return f"{size_in_bytes:.2f} {size_units[i]}"

def process_directory(directory, output_directory):
    """Process all HTML files in the directory and convert them to PDF."""
    html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
    total_files = len(html_files)
    total_pdf_size = 0
    processed_files = 0

    if total_files == 0:
        print(f"{Fore.YELLOW}No HTML files found in the directory.")
        return

    print(f"{Fore.CYAN}Converting {total_files} HTML files to PDF...")

    # Create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Process each HTML file and convert to PDF
    for html_file in tqdm(html_files, desc="Progress", unit="file", colour="green"):
        html_path = os.path.join(directory, html_file)
        pdf_file = os.path.join(output_directory, os.path.splitext(html_file)[0] + '.pdf')
        pdf_size = convert_html_to_pdf(html_path, pdf_file)
        if pdf_size > 0:
            total_pdf_size += pdf_size
            processed_files += 1

    # Display results
    total_size_formatted = format_size(total_pdf_size)
    print(f"{Fore.GREEN}Conversion complete! {processed_files}/{total_files} files processed.")
    print(f"{Fore.BLUE}Total size of all PDF files: {total_size_formatted}")

def main():
    while True:
        # Prompt user for the directory containing HTML files
        directory = input(f"{Fore.MAGENTA}Enter the directory containing HTML files (or type 'e'/'exit' to quit): {Style.BRIGHT}")
        
        if directory.lower() in ['e', 'exit']:
            print(f"{Fore.YELLOW}Exiting the program.")
            break
        
        if not os.path.isdir(directory):
            print(f"{Fore.RED}Invalid directory. Please try again.")
            continue

        # Prompt user for the output directory
        default_output_dir = f"./{os.path.basename(directory)}_{datetime.now().strftime('%Y%m%d')}/"
        output_directory = input(f"{Fore.MAGENTA}Enter the output directory for PDF files (leave blank to use '{default_output_dir}'): {Style.BRIGHT}")
        
        # Use the default output directory if the input is blank
        if not output_directory.strip():
            output_directory = default_output_dir
        
        # Process the directory
        process_directory(directory, output_directory)
        
        # Ask if the user wants to process another directory
        again = input(f"{Fore.CYAN}Do you want to process another directory? (y/n): {Style.BRIGHT}")
        if again.lower() != 'y':
            print(f"{Fore.YELLOW}Goodbye!")
            break

if __name__ == '__main__':
    main()
