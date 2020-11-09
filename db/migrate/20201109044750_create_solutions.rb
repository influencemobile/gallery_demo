class CreateSolutions < ActiveRecord::Migration[6.0]
  def change
    create_table :solutions do |t|
      t.text :description
      t.text :painting
      t.text :artist
      t.text :gallery

      t.timestamps
    end
  end
end
