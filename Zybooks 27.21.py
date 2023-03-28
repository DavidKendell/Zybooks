row, col = [int(i) for i in input().split(" ")]
print("<table>")
print(f"<tr> {' '.join(['<td> c </td>']*col)} </tr>\n" * row, end="")
print("</table>")