import random
import string
import numpy as np
from sklearn.linear_model import LinearRegression

def generate_commit_message(type, severity):
    """Generates a commit message."""
    words = ["fixed", "bug", "issue", "regression"]
    if severity == "critical":
        words += ["critical", "important", "urgent"]
    elif severity == "major":
        words += ["major", "important"]
    elif severity == "minor":
        words += ["minor", "cosmetic"]
    return " ".join(random.sample(words, 3))

def generate_release_notes(type, severity):
    """Generates release notes."""
    words = ["This release includes", "We are excited to announce", "We fixed a few bugs", "We added a new feature", "We improved performance", "We refactored the code"]
    if type == "bug_fix":
        words += [f"{type} in {severity}"]
    elif type == "feature":
        words += [f"{type} in {severity}"]
    else:
        words += [f"{type}"]
    return " ".join(random.sample(words, 5))

def generate_pull_request_title(type, severity):
    """Generates a pull request title."""
    words = ["Add", "Fix", "Update", "Remove", "Change", "Improve", "Optimize", "Refactor"]
    if type == "bug_fix":
        words += [f"{type} {severity}"]
    elif type == "feature":
        words += [f"{type} {severity}"]
    else:
        words += [f"{type}"]
    return " ".join(random.sample(words, 2))

def generate_review_comment(rating):
    """Generates a review comment."""
    words = ["This is a great pull request!", "The new feature is very useful", "The code is well-written", "I have a few minor suggestions", "Overall, I think this is ready to be merged"]
    if rating == 10:
        words += ["This is a great pull request! I highly recommend merging it."]
    elif rating == 8:
        words += ["This is a good pull request. I recommend merging it with some minor changes."]
    elif rating == 6:
        words += ["This is a pull request that could be improved. I recommend making some changes before merging it."]
    elif rating == 4:
        words += ["This is a pull request that should not be merged. I recommend rejecting it."]
    return " ".join(random.sample(words, 5))

def generate_rating():
    """Generates a rating based on the functions discussed."""
    code_coverage = random.uniform(70, 100)
    merge_conflicts = random.randint(0, int(code_coverage / 2))
    code_smells = random.randint(0, int(code_coverage / 4))
    test_coverage = random.uniform(70, 100)
    pull_requests_merged = random.randint(0, int(code_coverage * 0.1))
    response_time_for_code_reviews = random.uniform(0, 48)
    average_code_complexity = random.uniform(1, 10)
    average_code_duplication = random.uniform(0, 10)
    features = np.array([code_coverage, merge_conflicts, code_smells, test_coverage, pull_requests_merged, response_time_for_code_reviews, average_code_complexity, average_code_duplication])
    rating = 10 * LinearRegression().fit(features.reshape(-1, 1), rating).predict(features.reshape(-1, 1))[0]
    # Add some noise to the numerical values.
    code_coverage += random.uniform(-10, 10)
    merge_conflicts += random.uniform(-5, 5)
    code_smells += random.uniform(-2, 2)
    test_coverage += random.uniform(-10, 10)
    pull_requests_merged += random.uniform(-5, 5)
    response_time_for_code_reviews += random.uniform(-16, 16)
    return rating

def generate_data(num_samples):
    data = []
    for _ in range(num_samples):
        commit_id = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
        commit_hash = "".join(random.choices(string.ascii_lowercase + string.digits, k=16))
        commit_author = random.choice(["John Doe", "Jane Smith", "Alex Johnson"])
        commit_message = generate_commit_message(random.choice(["bug_fix", "feature", "refactoring"]), random.choice(["critical", "major", "minor"]))
        release_version = "v" + str(random.randint(1, 10)) + "." + str(random.randint(0, 9))
        release_date = random.choice(["2023-01-01", "2023-02-01", "2023-03-01"])
        release_notes = generate_release_notes(random.choice(["bug_fix", "feature", "refactoring"]), random.choice(["critical", "major", "minor"]))
        successful_builds_per_day = random.uniform(80, 100)
        code_coverage = random.uniform(70, 100)
        open_issues = random.randint(0, 10)
        time_to_resolve_issues = random.uniform(0, 30)
        merge_conflicts = random.randint(0, int(code_coverage / 2))
        pipeline_success_rate = random.uniform(90, 100)
        active_contributors = random.randint(1, 5)
        avg_time_to_merge_pull_request = random.uniform(0, 10)
        closed_milestones = random.randint(0, 5)
        response_time_for_code_reviews = random.uniform(0, 48)
        code_complexity = random.uniform(1, 10)
        code_duplication = random.uniform(0, 10)
        code_smells = random.randint(0, int(code_coverage / 4))
        security_vulnerabilities_critical = random.randint(0, 5)
        security_vulnerabilities_moderate = random.randint(0, 10)
        test_coverage = random.uniform(70, 100)
        pull_request_id = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
        pull_request_title = generate_pull_request_title(random.choice(["bug_fix", "feature", "refactoring"]), random.choice(["critical", "major", "minor"]))
        reviewer = random.choice(["John Doe", "Jane Smith", "Alex Johnson"])
        review_comments = generate_review_comment(random.choice([4, 6, 8, 10]))
        review_duration = random.uniform(0, 7)
        pull_request_state = random.choice(["open", "closed", "merged"])
        time_from_ready_to_merge = random.uniform(0, 48)
        comments_follow_up_time = random.uniform(0, 48)
        time_spent_in_ready = random.uniform(0, 10)
        time_spent_in_in_review = random.uniform(0, 10)
        time_spent_in_merged = random.uniform(0, 48)
        pull_request_rate = random.uniform(0, 5)
        pull_request_duration = random.uniform(0, 10)
        merge_ratio = random.uniform(0, 100)
        num_in_progress_pull_requests = random.randint(0, 5)
        days_worked_between_pull_and_merge = random.uniform(0, 30)
        review_time = random.uniform(0, 7)
        code_churn = random.randint(1, 100)

        data.append([
            commit_id, commit_hash, commit_author, commit_message, release_version, release_date, release_notes,
            successful_builds_per_day, code_coverage, open_issues, time_to_resolve_issues, merge_conflicts,
            pipeline_success_rate, active_contributors, avg_time_to_merge_pull_request, closed_milestones,
            response_time_for_code_reviews, code_complexity, code_duplication, code_smells,
            security_vulnerabilities_critical, security_vulnerabilities_moderate, test_coverage, pull_request_id,
            pull_request_title, reviewer, review_comments, review_duration, pull_request_state,
            time_from_ready_to_merge, comments_follow_up_time, time_spent_in_ready, time_spent_in_in_review,
            time_spent_in_merged, pull_request_rate, pull_request_duration, merge_ratio,
            num_in_progress_pull_requests, days_worked_between_pull_and_merge, review_time, code_churn
        ])

    return data

# Generating a synthetic dataset with 100 samples
dataset = generate_data(100)

dataset.to_csv("BardGPT.csv")

# Printing the first few samples of the dataset
for sample in dataset[:5]:
    print(sample)
