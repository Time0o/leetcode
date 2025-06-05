def solution(words: list[str], max_width: int) -> list[str]:
     lines = []
     line = []
     line_width = 0
     line_content_width = 0

     i = 0
     while i < len(words):
         line_width_next = line_width + len(words[i]) + bool(line)

         if line_width_next <= max_width:
             line.append(words[i])
             line_width = line_width_next
             line_content_width += len(words[i])
             i += 1
         else:
             if len(line) == 1:
                 line_justified = line[0].ljust(max_width)
             else:
                 total_space = max_width - line_content_width
                 avg_space = total_space // (len(line) - 1)
                 leftover_space = total_space % (len(line) - 1)

                 line_with_space = []
                 for j, w in enumerate(line):
                     line_with_space.append(w)
                     if j < len(line) - 1:
                         space = " " * (avg_space + (j < leftover_space))
                         line_with_space.append(space)

                 line_justified = "".join(line_with_space)

             lines.append(line_justified)

             line.clear()
             line_width = 0
             line_content_width = 0

     final_line = " ".join(line).ljust(max_width)
     lines.append(final_line)

     return lines
