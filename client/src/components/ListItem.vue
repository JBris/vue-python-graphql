<template>
  <div class="column is-5">
    <CollapsibleCard :title="`${repo.author}/${repo.repo}`" id="`repo-item-${repo.id}`">
        <div class="panel-body">
          <p>{{ repo.description }}</p>
          <a :href="repo.htmlUrl" :target="`_blank`" rel="noopener noreferrer">Home</a>
          <a :href="repo.tagsUrl" :target="`_blank`" rel="noopener noreferrer">Tags</a>
          <a :href="repo.cloneUrl" :target="`_blank`" rel="noopener noreferrer">Clone</a>
        </div>  
    </CollapsibleCard>
  </div>
</template>

<script>
  import CollapsibleCard from "@/components/CollapsibleCard.vue";
  
  export default {
    name: 'ListItem',
    components: {
      CollapsibleCard
    },
    props:{
      repo:{
        type : Object,
        required:true
      },
    },
  };
</script>
