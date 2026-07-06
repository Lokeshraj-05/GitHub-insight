export default function RepoCard({

    repo

}) {

    return (

        <div style={card}>

            <h2>
                {repo.repo}
            </h2>

            <p>
                Category:
                {repo.type}
            </p>

            <hr/>

            <p>
                {
                    repo.analysis
                    .summary
                }
            </p>

        </div>
    );
}

const card = {

    background:"#1e293b",
    color:"white",
    padding:"20px",
    borderRadius:"20px",
    margin:"15px"
}