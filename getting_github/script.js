async function getData(element){
    let response = await fetch('https://api.github.com/users/adion81')
    let git_data = await response.json()
    console.log(git_data)
    let requestedData = git_data[element]
    let label = element.charAt(0).toUpperCase() + element.slice(1)
    field1.innerHTML = `
    <p>Name: ${git_data.name}</p>
    <p>Followers: ${git_data.followers}</p>
    <p>Public Repos: ${git_data.public_repos}</p>
    <p>${label}: ${requestedData}</p>
    `
    return git_data
}
