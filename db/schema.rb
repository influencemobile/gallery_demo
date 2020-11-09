# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `rails
# db:schema:load`. When creating a new database, `rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 2020_11_09_044750) do

  create_table "artists", force: :cascade do |t|
    t.string "name"
    t.integer "age"
    t.integer "experience_level"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "galleries", force: :cascade do |t|
    t.string "name"
    t.string "location"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "paintings", force: :cascade do |t|
    t.string "name"
    t.integer "price"
    t.integer "artist_id", null: false
    t.integer "gallery_id", null: false
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
    t.index ["artist_id"], name: "index_paintings_on_artist_id"
    t.index ["gallery_id"], name: "index_paintings_on_gallery_id"
  end

  create_table "results", force: :cascade do |t|
    t.text "description"
    t.integer "value"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "solutions", force: :cascade do |t|
    t.text "description"
    t.text "painting"
    t.text "artist"
    t.text "gallery"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  add_foreign_key "paintings", "artists"
  add_foreign_key "paintings", "galleries"
end
