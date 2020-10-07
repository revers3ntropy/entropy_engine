import entropy_engine as ee
ee.init((100, 100))


test_file = ee.game_data_manager.new_file('test')
test_file.load()

ee.run_game()
