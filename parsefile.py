from collections import defaultdict
import pysam

samfile = pysam.AlignmentFile("bowtie2-sorted.bam", "rb")

gcs = {} 
gcs = defaultdict(lambda:[0, 0, 0], gcs)

total = 0
gc_total = 0

# get all reads from the alignment. order of reads does not matter.
for read in samfile.fetch():
    read_sequence = read.query_sequence
    window_start = read.reference_start // 100
    # use the contig name and the start of the alignment within the contig (rounded down to 100s) as an identifier.
    window_name = '{}-{}'.format(read.reference_name, window_start)
    gcs[window_name][0] += len(read_sequence)
    gcs[window_name][1] += len([base for base in read_sequence if base == 'C' or base == 'G'])
    gcs[window_name][2] += 1

# output formatted for csv file. redirect output to preferred file.
print('contig window number,position in contig,number of reads starting in window,%GC content')
for window in gcs:
    contig_window = int(window.split('-')[1]) * 100
    print('{},{}-{},{},{}'.format(window, contig_window, contig_window + 100, gcs[window][2], gcs[window][1] / gcs[window][0]))
