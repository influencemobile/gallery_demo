require 'faker'
Artist.destroy_all
Gallery.destroy_all
Painting.destroy_all

6.times do
  Artist.create(name: Faker::Artist.name, age: Faker::Number.between(from: 15, to: 100), experience_level: Faker::Number.between(from: 10, to: 1000))
end

4.times do
  Gallery.create(name: Faker::Hipster.word, location: Faker::Nation.capital_city)
end

20.times do
  Painting.create(name: Faker::Hipster.word, price: Faker::Number.between(from: 100, to: 500000), artist_id: Artist.ids.sample, gallery_id: Gallery.ids.sample)
end