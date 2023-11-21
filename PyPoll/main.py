import os
import csv


def load_election_data(file_path):
    candidates = []
    num_votes = []
    percent_votes = []
    total_votes = 0

    with open(file_path, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        csv_header = next(csvreader)

        for row in csvreader:
            total_votes += 1

            if row[2] not in candidates:
                candidates.append(row[2])
                index = candidates.index(row[2])
                num_votes.append(1)
            else:
                index = candidates.index(row[2])
                num_votes[index] += 1

        for votes in num_votes:
            percentage = (votes / total_votes) * 100
            percentage = "%.3f%%" % percentage
            percent_votes.append(percentage)

        winner_votes = max(num_votes)
        winner_index = num_votes.index(winner_votes)
        winner_candidate = candidates[winner_index]

    return candidates, num_votes, percent_votes, total_votes, winner_candidate


def print_results(candidates, num_votes, percent_votes, total_votes, winner_candidate):
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------------")

    for candidate, votes, percentage in zip(candidates, num_votes, percent_votes):
        print(f"{candidate}: {percentage} ({votes})")

    print("--------------------------")
    print(f"Winner: {winner_candidate}")
    print("--------------------------")


def export_results_to_txt(output_file_path, candidates, num_votes, percent_votes, total_votes, winner_candidate):
    with open(output_file_path, "w") as output:
        output.write("Election Results\n")
        output.write("--------------------------\n")
        output.write(f"Total Votes: {total_votes}\n")
        output.write("--------------------------\n")

        for candidate, votes, percentage in zip(candidates, num_votes, percent_votes):
            output.write(f"{candidate}: {percentage} ({votes})\n")

        output.write("--------------------------\n")
        output.write(f"Winner: {winner_candidate}\n")
        output.write("--------------------------\n")


def main():
    file_to_load = os.path.join("election_data.csv")
    candidates, num_votes, percent_votes, total_votes, winner_candidate = load_election_data(file_to_load)

    print_results(candidates, num_votes, percent_votes, total_votes, winner_candidate)

    output_file_path = "output_PyPoll.txt"
    export_results_to_txt(output_file_path, candidates, num_votes, percent_votes, total_votes, winner_candidate)


if __name__ == "__main__":
    main()
