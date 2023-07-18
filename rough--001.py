import matplotlib.pyplot as plt

credit = [146000, 131000]
labels = ['Credit History', 'No Credit History']

plt.bar(labels, credit)
plt.ylabel("Average Loan Amount")
plt.title("Loan Amount by Credit History")

plt.show()