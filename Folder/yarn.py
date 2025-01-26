### yarn.py

#inputs 
yarn_needed = int(input('Enter amount of yarn required for the project (m): '))
pack_mtrs = int(input('Enter meters of yarn in a pack: '))

# caculating amount of yarn needed
packs_needed = (yarn_needed // pack_mtrs) + 1

print('Number of packs required for the project: ', str(packs_needed))