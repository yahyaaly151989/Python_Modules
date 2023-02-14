# ========================== statistics Module ==========================
import statistics as st

# print(dir(st))

# print(st.mean( [2, 4, 3] ))
# print(st.mean( (2, 4, 3) ))
# print(st.mean( {2, 4, 3} ))
# print(st.mean( {2: "two", 4: "four", 3: "three"} ))

# print(st.harmonic_mean([1, 2, 3]))

# # print(st.median( [2, 4, 3, 5, 9, 13, 17] )) # [2, 3, 4, 5, 9, 13, 17]
# print(st.median( [2, 4, 3, 5, 9, 13] )) # [2, 3, 4, 5, 9, 13]
# print(st.median_low( [2, 4, 3, 5, 9, 13, 17] )) # [2, 3, 4, 5, 9, 13, 17]
# print(st.median_high( [2, 4, 3, 5, 9, 13, 17] )) # [2, 3, 4, 5, 9, 13, 17]
# print(st.median_low( [2, 4, 3, 5, 9, 13] )) # [2, 3, 4, 5, 9, 13]
# print(st.median_high( [2, 4, 3, 5, 9, 13] )) # [2, 3, 4, 5, 9, 13]

# print(st.mode( [1, 2, 3, 2] ))
# print(st.mode( [1, 2, 3, 3, 2] ))
# print(st.mode( [1, 2] ))

print(st.stdev([1, 2, 100]))

print(st.variance([1, 2, 3]))
