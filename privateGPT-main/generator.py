import random
import csv
import math

# Define the range and parameters for generating synthetic data
num_rows = 5000

# Define the weights for each attribute
weights = {
    'Successful_Builds_per_Day': 0.3,
    'Code_Coverage': 0.2,
    'Time_to_Resolve_Issues': 0.25,
    'Average_Time_to_Merge': 0.15,
    'Code_Complexity': 0.1,
    'Number_of_InProgress_PRs': 0.1
}

# Define the normalization parameters for the rating
rating_min = 0
rating_max = 10

# Open the CSV file to write the generated data
with open('mobile_banking_dataset.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    headers = ['Commit_Message', 'Release_Notes', 'Pull_Request_Title', 'Successful_Builds_per_Day', 'Code_Coverage',
               'Time_to_Resolve_Issues', 'Average_Time_to_Merge', 'Code_Complexity', 'Rating']
    writer.writerow(headers)

    # Generate the dataset
    for _ in range(num_rows):
        # Generate random values within the desired range for each attribute
        successful_builds = random.randint(80, 100)
        code_coverage = random.randint(70, 95)
        time_to_resolve_issues = random.randint(1, 30)
        average_time_to_merge = random.randint(1, 10)
        code_complexity = random.randint(5, 8)

        # Generate real-life examples for commit message, release notes, and pull request title
        commit_message = "Real-life example of commit message"
        release_notes = "Real-life example of release notes"
        pull_request_title = "Real-life example of pull request title"

        # Calculate the attributes based on the defined equations and correlations
        pipeline_success_rate = 0.8 * successful_builds
        test_coverage = code_coverage
        time_to_merge = 2 ** time_to_resolve_issues
        code_duplication = 10 - code_complexity
        active_contributors = random.randint(5, 15)
        in_progress_prs = int(math.log(active_contributors))
        rating = (weights['Successful_Builds_per_Day'] * successful_builds +
                  weights['Code_Coverage'] * code_coverage +
                  weights['Time_to_Resolve_Issues'] * time_to_merge +
                  weights['Average_Time_to_Merge'] * average_time_to_merge +
                  weights['Code_Complexity'] * code_complexity +
                  weights['Number_of_InProgress_PRs'] * in_progress_prs)

        # Normalize the rating to ensure it is between 0 and 10
        rating = (rating - rating_min) / (rating_max - rating_min) * 10

        # Write the generated row to the CSV file
        writer.writerow([commit_message, release_notes, pull_request_title, successful_builds, code_coverage,
                         time_to_resolve_issues, average_time_to_merge, code_complexity, rating])
