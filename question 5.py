# Question 5

# Create a list containing the titles of four TV programmes and display them on separate lines. Ask the
# user to enter another show and a position they want it inserted into the list. Display the list again,
# showing all five TV programmes in their new positions..


# Create a list containing the titles of four TV programmes
tv_programmes = ["Breaking Bad", "Friends", "Game of Thrones", "Stranger Things"]

# Display the original list of TV programmes
print("Original list of TV programmes:")
for programme in tv_programmes:
    print(programme)

# Ask the user to enter another show and the position to insert it into
new_show = input("\nEnter the name of another TV show: ")
position = int(input("Enter the position (0-4) where you want to insert the show: "))

# Check if the position is valid
if 0 <= position <= len(tv_programmes):
    # Insert the new show at the specified position
    tv_programmes.insert(position, new_show)
    
    # Display the updated list of TV programmes
    print("\nUpdated list of TV programmes:")
    for programme in tv_programmes:
        print(programme)
else:
    print("Invalid position! Please enter a valid position between 0 and 4.")
