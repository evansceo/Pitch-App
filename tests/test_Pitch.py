from models import Comment,User,Pitch
from app import db
import unittest

class PitchModelTest(unittest.TestCase):
    def setUp(self):
        self.user_Peris = User(username = 'Peris',password = 'banana', email = 'james@ms.com')
        self.new_pitch = Pitch(id=1,pitch_title='Test',pitch_content='This is a test pitch',category="interview",user = self.user_Peris,likes=0,dislikes=0)

    def tearDown(self):
        User.query.delete()
        Pitch.query.delete()
      

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_title,'Test')
        self.assertEquals(self.new_pitch.pitch_content,'This is a test pitch')
        self.assertEquals(self.new_pitch.category,"interview")
        self.assertEquals(self.new_pitch.user,self.user_Peris)

