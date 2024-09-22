# PeoplePerHour Job Scrapper

This is a Python script that uses the Scrapy library to scrape job data from the PeoplePerHour website.

## How to use

1. Install the requirements by running `pip install -r requirements.txt`
2. Change into the `scrapper` directory by running `cd scrapper`
3. Run the script by executing `scrapy crawl people_per_hour`

## Output

The script will output a JSON file in the output directory. The file will contain an array of job objects, each with the following properties:

- `username`: The username of the person who posted the job
- `profile_url`: The URL of the person's profile
- `price`: The price of the job
- `job_type`: The type of job (e.g. "opportunity")
- `job_title`: The title of the job
- `job_url`: The URL of the job
- `description`: The description of the job
- `posted_time`: The time the job was posted
- `num_proposals`: The number of proposals the job has received
- `location`: The location of the job

## License

This script is licensed under the MIT license. See the LICENSE file for more information.
