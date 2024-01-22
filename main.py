def calculate_average(grades):
  total = sum(grades)
  average = total / len(grades)
  return average

def assign_letter_grade(average):
  if 90 <= average <= 100:
      return 'A'
  elif 80 <= average < 90:
      return 'B'
  elif 70 <= average < 80:
      return 'C'
  elif 60 <= average < 70:
      return 'D'
  else:
      return 'F'

def main():
  # Get the number of grades from the user
  num_grades = int(input("Enter the number of grades: "))

  # Get the grades from the user
  grades = []
  for i in range(num_grades):
      grade = float(input(f"Enter grade {i + 1}: "))
      grades.append(grade)

  # Calculate the average
  average = calculate_average(grades)

  # Assign the letter grade
  letter_grade = assign_letter_grade(average)

  # Display the results
  print(f"\nAverage Grade: {average:.2f}")
  print(f"Letter Grade: {letter_grade}")

if __name__ == "__main__":
  main()