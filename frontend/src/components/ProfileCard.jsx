export default function ProfileCard({

    profile,
    score,
    rating

}) {

    return (

        <div style={card}>

            <h2>
                {profile.name}
            </h2>

            <p>
                {profile.bio}
            </p>

            <hr/>

            <p>
                Repositories :
                {profile.repositories}
            </p>

            <p>
                Followers :
                {profile.followers}
            </p>

            <p>
                GitHub Score :
                {score}/100
            </p>

            <h3>
                Rating :
                {rating}
            </h3>

        </div>
    );
}

const card = {

    background:"#111827",
    color:"white",
    padding:"20px",
    borderRadius:"20px",
    margin:"20px"
}