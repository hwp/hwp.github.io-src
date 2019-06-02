#!/usr/bin/env bash
BRANCH=master
GITIO_REPO=git@github.com:hwp/hwp.github.io.git
GITIO_REPO_PATH=gitio_repo
PELICAN_OUT_PATH=output

# get head reference number
headref=$(git show-ref HEAD)

# clone io repo
git clone --branch=$BRANCH $GITIO_REPO $GITIO_REPO_PATH || echo 'github.io repo exist' &&

# copy data we're interested in to that directory
rsync -av --delete --exclude=.git $PELICAN_OUT_PATH/ $GITIO_REPO_PATH/ &&

# go into
cd $GITIO_REPO_PATH &&

# add, commit and push files
git add -f . &&
git commit -m "Deploy '$headref' to Github Pages" &&
git push origin $BRANCH > /dev/null &&

echo 'Deploy completed' || echo 'Deploy failed'

