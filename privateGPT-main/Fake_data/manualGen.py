import random
import string
import csv
import math
import datetime
start_date = datetime.datetime(2023, 1, 1)  # Specify the starting date

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
    words = [
        "This release includes",
        "We are excited to announce",
        "We fixed a few bugs",
        "We added a new feature",
        "We improved performance",
        "We refactored the code",
    ]
    if type == "bug_fix":
        words += [f"{type} in {severity}"]
    elif type == "feature":
        words += [f"{type} in {severity}"]
    else:
        words += [f"{type}"]
    return " ".join(random.sample(words, 5))


def generate_pull_request_title(type, severity):
    """Generates a pull request title."""
    words = [
        "Add",
        "Fix",
        "Update",
        "Remove",
        "Change",
        "Improve",
        "Optimize",
        "Refactor",
    ]
    if type == "bug_fix":
        words += [f"{type} {severity}"]
    elif type == "feature":
        words += [f"{type} {severity}"]
    else:
        words += [f"{type}"]
    return " ".join(random.sample(words, 2))


def generate_review_comment(rating):
    """Generates a review comment."""
    words = [
        "This is a great pull request!",
        "The new feature is very useful",
        "The code is well-written",
        "I have a few minor suggestions",
        "Overall, I think this is ready to be merged",
    ]
    if rating >= 8.5:
        words += ["This is a great pull request! I highly recommend merging it."]
    elif rating >= 7 and rating < 8.5:
        words += [
            "This is a good pull request. I recommend merging it with some minor changes."
        ]
    elif rating >= 5.5 and rating <7:
        words += [
            "This is a pull request that could be improved. I recommend making some changes before merging it."
        ]
    else :
        words += [
            "This is a pull request that should not be merged. I recommend rejecting it."
        ]
    return " ".join(random.sample(words, 5))


def generate_rating():
    """Generates a rating based on the functions that we discussed."""
    rating = random.randint(2, 10)
    code_coverage = max(min(100 - (50 / random.uniform(rating-0.3, rating + 0.3)), 100), 0)
    merge_conflicts = random.randint(0, min(int(10 / rating) + 1, 10))
    code_smells = random.randint(0, 50 - 5 * int(code_coverage / 10))
    test_cases = int(min(code_coverage * 2, 500))
    pull_requests_merged = int(min((code_coverage / 100) * 2, 10))
    response_time_for_code_reviews = int(min(code_coverage / 10, random.randint(0, 2)))

    average_code_complexity = min(random.randint(1, int(200 / code_coverage)), 50) + 8
    average_code_duplication = max(
        min(random.randint(1, int(code_coverage / 4)), 100), 0
    )
    security_vulnerabilities = 1 if rating < random.randint(4,6) else 0

    # Hna kayen probleme
    pipeline_success_rate = 1 if rating > random.randint(6,8) else 0

    time_to_resolve_issues = int(min(max((security_vulnerabilities / 2) + 5, 1), 100))
    open_issues = int(min(max((code_smells / 4), 0), 100))

    # rating = (
    #     0.7 * math.exp(math.sqrt(code_coverage/5))
    #     + 0.5 * pipeline_success_rate
    #     - 0.6 * security_vulnerabilities
    #     - 0.3 * merge_conflicts
    #     + 1
    #     - 0.1 * open_issues
    #     + 0.05 * time_to_resolve_issues
    #     - 0.02 * code_smells
    #     + 0.01 * test_cases
    #     + 0.03 * pull_requests_merged
    #     + 0.01 * response_time_for_code_reviews
    #     - 0.001 * average_code_complexity
    #     - 0.002 * average_code_duplication
    # )

    rating = (
    0.7 * (1 - math.exp(-code_coverage/100))
    + 0.55 * (1 - math.exp(-pipeline_success_rate))
    - 0.6 * math.log(1 + security_vulnerabilities)
    - 0.3 * math.log(1 + merge_conflicts/10)
    + 1
    - 0.1 * open_issues
    + 0.05 * (1 - math.exp(-time_to_resolve_issues))
    - 0.02 * math.log(1 + code_smells/50)
    + 0.01 * test_cases/200
    + 0.03 * pull_requests_merged/10
    + 0.01 * (1 - math.exp(-response_time_for_code_reviews/3))
    - 0.001 * average_code_complexity/20
    - 0.002 * average_code_duplication/20
    )

    # code_coverage += random.uniform(-3, 3)
    # merge_conflicts += int(random.uniform(-5, 5))
    # code_smells += int(random.uniform(-2, 2))
    # test_cases += int(random.uniform(-4, 4))
    # pull_requests_merged += int(random.uniform(-2, 2))
    # response_time_for_code_reviews += int(random.uniform(-1, 1))
    # average_code_complexity += random.uniform(-4, 4)
    # average_code_duplication += random.uniform(-2, 2)

    code_coverage += random.uniform(random.uniform(-3, 0), random.uniform(0, 3))
    merge_conflicts += int(random.uniform(-5, 5))
    code_smells += int(random.uniform(-2, 2))
    test_cases += int(random.uniform(-4, 4))
    pull_requests_merged += int(random.uniform(-2, 2))
    response_time_for_code_reviews += int(random.uniform(-1, 1))
    average_code_complexity += random.uniform(-4, 4)
    average_code_duplication += random.uniform(-2, 2)
    open_issues += random.randint(0, 2)

    if open_issues == 0:
        time_to_resolve_issues = 0
    else:
        time_to_resolve_issues += open_issues * random.randint(0, 3)

    code_coverage = max(min(code_coverage, 100), 0)
    merge_conflicts = max(min(merge_conflicts, 10), 0)
    code_smells = max(min(code_smells, 100), 0)
    test_cases = max(min(test_cases, 500), 0)
    pull_requests_merged = max(min(pull_requests_merged, 10), 0)
    response_time_for_code_reviews = max(min(response_time_for_code_reviews, 10), 0)
    average_code_complexity = max(min(average_code_complexity, 50), 1)
    average_code_duplication = max(min(average_code_duplication, 100), 0)

    rating = (rating - 0.1)/(2 - 0.1) * 10 # 75
    rating += random.uniform(random.uniform(-0.5, 0), random.uniform(0,0.5))


    return rating, code_coverage, merge_conflicts,pipeline_success_rate, code_smells, test_cases, pull_requests_merged, response_time_for_code_reviews, average_code_complexity, average_code_duplication, time_to_resolve_issues, open_issues


def append_row_to_csv(row, filename):
    """Appends a row to the CSV file."""
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)


# Generate and export the synthetic dataset
filename = "software_dev_dataset.csv"
header = [
    "Commit ID",
    "Commit Hash",
    "Commit Author",
    "Commit Message",
    "Release Version",
    "Release Date",
    "Release Notes",
    "Successful Builds per Day",
    "Code Coverage",
    "Open Issues",
    "Time to Resolve Issues",
    "Merge Conflicts",
    "Pipeline Success Rate",
    "Active Contributors",
    "Average Time to Merge",
    "Closed Milestones",
    "Response Time for Code Reviews",
    "Average Code Complexity",
    "Average Code Duplication",
    "Test Coverage",
    "Pull Request ID",
    "Pull Request Title",
    "Reviewer",
    "Review Comments",
    "Review Duration",
    "Pull Request State",
    "Time from Ready to Merge",
    # "Comments Follow-up Time",
    # "Time Spent in Ready",
    # "Time Spent in In Review",
    # "Time Spent in Merged",
    "Pull Request Rate",
    "Pull Request Duration",
    "Merge Ratio",
    "Number of In-Progress Pull Requests",
    "Days Worked between Pull and Merge Confirmation",
    # "Review Time",
    "Code Churn",
    "Rating",
]

def generate_release_version(iterator):
    # Generate the release version components
    X = iterator // 100000
    YY = (iterator % 100000) // 1000
    ZZZZ = iterator % 1000

    if ZZZZ == 0:
        ZZZZ = 9999
        YY -= 1

    if YY == -1:
        YY = 99
        X -= 1

    release_version = 'v'+ '.'.join([str(int(part)) for part in f"{X}.{YY:02d}.{ZZZZ:04d}".split(".")])
    if iterator == 0 : 
        release_version = "v0.0.0"
    return release_version
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)

for i in range(1000):
    type = random.choice(["bug_fix", "feature", "documentation"])
    severity = random.choice(["critical", "major", "minor"])
    (
        rating,
        code_coverage,
        merge_conflicts,
        pipeline_success_rate,
        code_smells,
        test_cases,
        pull_requests_merged,
        response_time_for_code_reviews,
        average_code_complexity,
        average_code_duplication,
        time_to_resolve_issues,
        open_issues,
    ) = generate_rating()
    commit_message = generate_commit_message(type, severity)
    release_notes = generate_release_notes(type, severity)
    pull_request_title = generate_pull_request_title(type, severity)
    review_comment = generate_review_comment(rating)

    commit_id = str(i).zfill(7)
    commit_hash = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    commit_author = random.choice(
        ["Hicham", "Safae", "Oussama", "Karim"]
    )
    
    release_version = generate_release_version(i)
    # release_version = 'v'+ '.'.join([str(int(part)) for part in f"{i // 100}.{(i % 100) // 10:02d}.{i % 10:04d}".split(".")])
    
    if random.randint(0,15) < 1: 
        release_date = (start_date + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        start_date = start_date + datetime.timedelta(days=1)
    else : 
        release_date = (start_date).strftime("%Y-%m-%d")
    successful_builds_per_day = random.randint(90, 100)
    # pipeline_success_rate = random.randint(90, 100)
    active_contributors = random.randint(3, 10)
    average_time_to_merge = random.uniform(1, 5)
    closed_milestones = random.randint(1, 5)
    # response_time_for_code_reviews = int(code_coverage * 8)
    test_coverage = test_cases
    pull_request_id = i + 1
    reviewer = random.choice(["Soufyane", "Wiame"])
    review_comments = random.randint(0, 5) # TO BE CHECKED
    review_duration = random.randint(1, 4)
    pull_request_state = random.choice(["Open", "Merged", "Closed"])
    time_from_ready_to_merge = random.randint(1, 4)  # Add code here
    try : 
        pull_request_rate = (
        pull_requests_merged / (start_date - datetime.datetime(2023, 1, 1)).days
        )
    except : 
        pull_request_rate = None
    
    try : 
        pull_request_duration = int(
            time_from_ready_to_merge * pull_request_rate
        ) * 100
    except : 
        pull_request_duration =  None
    try : 
        merge_ratio = pull_requests_merged / (pull_requests_merged + open_issues)
    except : 
        merge_ratio = None
    num_in_progress_pull_requests = random.randint(0, 5)
    days_worked_between_pull_and_merge_confirmation = (
        time_to_resolve_issues + time_from_ready_to_merge
    )
    code_churn = int(
        code_smells + merge_conflicts + (test_cases / 2) + (pull_requests_merged / 5)
    ) * 2

    row = [
        commit_id,
        commit_hash,
        commit_author,
        commit_message,
        release_version,
        release_date,
        release_notes,
        successful_builds_per_day,
        code_coverage,
        open_issues,
        time_to_resolve_issues,
        merge_conflicts,
        pipeline_success_rate,
        active_contributors,
        average_time_to_merge,
        closed_milestones,
        response_time_for_code_reviews,
        average_code_complexity,
        average_code_duplication,
        test_coverage,
        pull_request_id,
        pull_request_title,
        reviewer,
        review_comments,
        review_duration,
        pull_request_state,
        time_from_ready_to_merge,
        # comments_follow_up_time,
        # time_spent_in_ready,
        # time_spent_in_in_review,
        # time_spent_in_merged,
        pull_request_rate,
        pull_request_duration,
        merge_ratio,
        num_in_progress_pull_requests,
        days_worked_between_pull_and_merge_confirmation,
        # review_time,
        code_churn,
        rating,
    ]

    append_row_to_csv(row, filename)