import gql from 'graphql-tag'

export const SEARCH_QUERY = gql`query gitRepos($provider: Providers!, $project: String!, $quantity: Int!) {
   gitRepos(provider: $provider, project: $project, quantity: $quantity) {
      items {
         id
         repo 
         author  
         host 
         htmlUrl 
         tagsUrl  
         cloneUrl 
         description  
      }
   }
}`
    