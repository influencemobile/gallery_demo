
* clone github repo locally

* prerequisites
  * ruby version 2.5.8 or higher

  * sqlite3 (you might already have this)

* setup rails / project
  * `gem install bundler`
  * `bundle install`
  * `rake db:migrate`
  * `rake db:seed`

* run rails server

`rails s`

* view pages (confirm you see some data)

https://localhost:3000/artists

https://localhost:3000/galleries

https://localhost:3000/paintings


* Your Challenge...

  * please create a process, script, or webpage that will show us the following:

    * The average age of the artists

    * The average experience level of the artists

    * The highest priced painting, which artist created it, and what gallery it is in

    * The lowest priced painting, which artist created it, and what gallery it is in

    * The median (not average) priced painting, with artist and gallery

  * bonus points if you we can view these results in the web browser, but not required

  * the process can be triggered/refreshed manually, or automatically, or at time of viewing

  * bonus points for storing the results in a new table

  * the exercise is based on this excellent tutorial: https://medium.com/@gaidaescobar/build-a-very-basic-ruby-on-rails-app-e2ac88c47f8c
  
