# PeoplePerHour Job Scrapper

This is a Python script that uses the Scrapy library to scrape job data from the PeoplePerHour website.

## How to use

1. Install the Scrapy library by running `pip install scrapy`
2. Run the script by executing `python peopleperhour_scraper.py`
3. The script will start scraping the website and storing the data in a JSON file named `jobs.json`

## Configuration

You can configure the script by editing the `settings.py` file. The following options are available:

* `USER_AGENT`: The user agent string to use when making requests to the website. Defaults to `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3`
* `DOWNLOAD_DELAY`: The delay in seconds between requests. Defaults to `0.5`
* `CONCURRENT_REQUESTS`: The number of concurrent requests to make. Defaults to `16`
* `DEPTH_PRIORITY`: The priority of the depth of the crawl. Defaults to `0`
* `SCHEDULER_DISK_QUEUE`: The disk queue to use for storing requests. Defaults to `scrapy.squeues.PickleFifoDiskQueue`
* `SCHEDULER_MEMORY_QUEUE`: The memory queue to use for storing requests. Defaults to `scrapy.squeues.FifoMemoryQueue`

## Output

The script will output a JSON file named `jobs.json` in the same directory as the script. The file will contain an array of job objects, each with the following properties:

* `title`: The title of the job
* `description`: The description of the job
* `url`: The URL of the job
* `category`: The category of the job
* `location`: The location of the job
* `posted`: The date the job was posted
* `budget`: The budget for the job
* `bids`: The number of bids for the job
* `client`: The client who posted the job
* `payment_verified`: Whether the client has verified their payment details
* `job_type`: The type of job (hourly or fixed price)

## License

This script is licensed under the MIT license. See the LICENSE file for more information.
