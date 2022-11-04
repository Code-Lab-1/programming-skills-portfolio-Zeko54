guest_list= ['Armash' ,'Ahmed', 'Muntazir']
print('Sorry guys, I can only invite two people to the dinner.')
print('Sorry bro ' + guest_list[1] + 'You are not invited for dinner.')
guest_list.pop(1)
print(guest_list)

print('Dear ' + guest_list[0] +' you are still invited to the dinner')
print('Dear ' + guest_list[1] +' you are still invited to the dinner')

del guest_list[:]
print('Guest list:', guest_list)