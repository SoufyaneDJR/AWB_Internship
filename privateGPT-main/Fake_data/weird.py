string_ = ["commit_id","commit_hash","commit_author","commit_message","release_version","release_date","release_notes","successful_builds_per_day","code_coverage","open_issues","time_to_resolve_issues","merge_conflicts","pipeline_success_rate","active_contributors","average_time_to_merge","closed_milestones","response_time_for_code_reviews","average_code_complexity","average_code_duplication","test_coverage","pull_request_id","pull_request_title","reviewer","review_comments","review_duration","pull_request_state","time_from_ready_to_merge","comments_follow_up_time","time_spent_in_ready","time_spent_in_in_review","time_spent_in_merged","pull_request_rate","pull_request_duration","merge_ratio","num_in_progress_pull_requests","days_worked_between_pull_and_merge_confirmation","review_time","code_churn","rating"]

list_ =["rating","code_coverage","merge_conflicts","code_smells","test_cases","pull_requests_merged","response_time_for_code_reviews","average_code_complexity","average_code_duplication"]
for el in list_ :
    try :
        string_.remove(el)
    except : 
        print(el)

print(string_)
