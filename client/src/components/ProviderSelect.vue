<template>
    <div class="provider-list">
        <select v-model="provider">
          <option disabled value="">Select platform...</option>
          <option v-for="provider in providers" v-bind:key="provider.value" v-bind:value="provider.value">
            {{ provider.text }}
          </option>
        </select>
    </div>
</template>

<script>
  export default {
    name: 'ProviderList',
    data () {
      return {
        providers: [
          { text: 'GitHub', value: 'GITHUB' },
          { text: 'Bitbucket', value: 'BITBUCKET' },
          { text: 'GitLab', value: 'GITLAB' }
        ],
      }
    },
    computed: {
      provider: {
        get () {
          return this.$store.state.provider
        },
        set (value) {
          this.$store.commit('setProvider', value)
        }
      }
    }
  }
</script>
