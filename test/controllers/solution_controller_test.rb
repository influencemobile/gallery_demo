require 'test_helper'

class SolutionControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get solution_index_url
    assert_response :success
  end

end
