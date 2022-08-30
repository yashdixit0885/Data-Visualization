
import unittest


from python_repos import github_call

class RepoTests(unittest.TestCase):
    """Tests for API call status"""
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    headers = {'Accept':'application/vnd.github.v3+json'}
    r= github_call(url,headers=headers)

    def test_status_200(self):

        
        self.assertEqual(self.r.status_code,200)

    def test_reponse_display_total_repo(self):
        
        response_dict =self.r.json()
        total = response_dict['total_count']
        self.assertGreater(total,90000)
  

   


if __name__ == '__main__':
    unittest.main()