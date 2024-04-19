from streamlit import title, header, subheader, write, number_input

title('Maximum of three numbers')
header("Enter three numbers")
subheader("in the boxes below")
a = number_input()
b = number_input()
c = number_input()

write("**Maximum** _value_ :")
write(max(a,b,c))
