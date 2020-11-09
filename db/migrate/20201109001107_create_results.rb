class CreateResults < ActiveRecord::Migration[6.0]
  def change
    create_table :results do |t|
      t.text :description
      t.integer :value

      t.timestamps
    end
  end
end
