# def get_number(x: int):
#     n_dict = {
#         1: "ONE",
#         2: "TWO",
#         3: "THREE",
#         4: "FOUR",
#         5: "FIVE",
#         6: "SIX",
#         7: "SEVEN",
#         8: "EIGHT",
#         9: "NINE",
#         10: "TEN",
#         11: "ELEVEN",
#         12: "TWELVE",
#         13: "THIRTEEN",
#         14: "FOURTEEN",
#         15: "FIFTEEN",
#         16: "SIXTEEN",
#         17: "SEVENTEEN",
#         18: "EIGHTEEN",
#         19: "NINETEEN",
#     }
#
#     nc_dict = {
#         2: 'TWENTY',
#         3: 'THIRTY',
#         4: 'FOURTY',
#         5: 'FIFTY',
#         6: 'SIXTY',
#         7: 'SEVENTY',
#         8: 'EHGTHY',
#         9: 'NINETY',
#     }
#
#     if (x == 100):
#         return 'HUNDRED'
#
#     if (x < 20):
#         return n_dict[x]
#
#     nc = x // 10
#     r = x % 10
#
#     if (r == 0):
#         return nc_dict[nc]
#
#     return nc_dict[nc] + " " + get_number(r)

# i = int(input())
# r = i
# for x in range(1000):
#     nn = get_number(r)
#     r = len(nn)

# after 1000 all numbers will converto 4 (FOUR)
i = int(input())
print(4)


