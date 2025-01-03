import csv
import os

def extract_stats(file_path):
    stats = {}
    found_vars = set()
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith("simSeconds") and 'simSeconds' not in found_vars:
                stats['simSeconds'] = line.split()[1]
                found_vars.add('simSeconds')
            elif line.startswith("hostSeconds") and 'hostSeconds' not in found_vars:
                stats['hostSeconds'] = line.split()[1]
                found_vars.add('hostSeconds')
            elif line.startswith("system.cpu.cpi") and 'cpi' not in found_vars:
                stats['cpi'] = line.split()[1]
                found_vars.add('cpi')
            elif line.startswith("system.cpu.ipc") and 'ipc' not in found_vars:
                stats['ipc'] = line.split()[1]
                found_vars.add('ipc')

            # Stop if all desired variables have been founds
            if len(found_vars) == 4 :
                break

    return stats


def main():
    # benchmark_ISAOlevel_m5out
    # test = ['gcc_X86O0_m5out', 'gcc_X86O1_m5out', 'gcc_X86O2_m5out', 'gcc_X86O3_m5out', 'gcc_ARMO0_m5out', 'gcc_ARMO1_m5out', 'gcc_ARMO2_m5out', 'gcc_ARMO3_m5out',
    #         'bzip2_X86O0_m5out', 'bzip2_X86O1_m5out', 'bzip2_X86O2_m5out', 'bzip2_X86O3_m5out', 'bzip2_ARMO0_m5out', 'bzip2_ARMO1_m5out', 'bzip2_ARMO2_m5out', 'bzip2_ARMO3_m5out']
    
    test = ['gcc_X86O0_m5out', 'gcc_X86O1_m5out', 'gcc_X86O2_m5out', 'gcc_X86O3_m5out',
            'bzip2_X86O0_m5out', 'bzip2_X86O1_m5out', 'bzip2_X86O2_m5out', 'bzip2_X86O3_m5out'] 

    # Output CSV
    output_file = '/home/taz/Repos/581-isa-project/runData/allRuns.csv'
    results = []

    for i in test :
        directory_path = '/home/taz/Repos/581-isa-project/runData/' + i + '/'  # Change this to your directory path
        
        os.chdir(directory_path)
        filename = directory_path + "stats.txt"
        stats = extract_stats(filename)
        stats['filename'] = i  # Add the filename to the stats
        results.append(stats)

        # Write results to CSV
        with open(output_file, 'w+', newline='') as csvfile:
            fieldnames = ['filename', 'simSeconds',
                        'hostSeconds', 'cpi', 'ipc']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()  # Write the header
            for result in results:
                writer.writerow(result)  # Write each row of stats

        print(f"Results have been written to {output_file}")


if __name__ == "__main__":
    main()
