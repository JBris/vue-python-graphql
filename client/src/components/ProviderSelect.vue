<template>
  <div class="field">
    <label class="label">Platform</label>
    <div class="control">
      <div class="select is-primary is-normal">
          <select v-model="provider" @change="changeProvider()">
            <option v-for="provider in providers" v-bind:key="provider.value" v-bind:value="provider.value">
              {{ provider.text }}
            </option>
          </select>
      </div>
    </div>
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
    },
    methods: {
        changeProvider() {
          this.$emit('change_provider');
        }
    }
  }
</script>
